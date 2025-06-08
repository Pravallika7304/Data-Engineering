import os
from extract_commoncrawl import extract_commoncrawl
from extract_abr import extract_abr_data
from transform_merge import match_entities
import psycopg2

def load_to_db(data):
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME", "your_db"),
            user=os.getenv("DB_USER", "postgres"),
            password=os.getenv("DB_PASS", "your_password"),
            host=os.getenv("DB_HOST", "localhost"),
            port=os.getenv("DB_PORT", "5432")
        )
        cur = conn.cursor()

        for item in data:
            cur.execute("""
                INSERT INTO companies (
                    abn, entity_name, entity_type, status, address,
                    postcode, state, start_date, website, industry
                ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """, (
                item.get('abn'), item.get('entity_name'), item.get('entity_type'), item.get('status'),
                item.get('address'), item.get('postcode'), item.get('state'), item.get('start_date'),
                item.get('website'), item.get('industry')
            ))

        conn.commit()
    except Exception as e:
        print("❌ Error loading to database:", e)
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    print("🔹 Extracting ABR data...")
    abr_data = extract_abr_data("data/abr_sample.xml")  # adjust path if needed

    print("🔹 Extracting Common Crawl data...")
    cc_data = extract_commoncrawl("data/common_crawl_sample.json")  # adjust path if needed

    print("🔹 Matching entities...")
    merged_data = match_entities(abr_data, cc_data)

    print("🔹 Loading into PostgreSQL...")
    load_to_db(merged_data)

    print("✅ Pipeline completed successfully.")
