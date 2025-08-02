"""
Data migration script to populate SQLite database with existing celebrity data
Run this script once to migrate from dictionary-based storage to database
"""

from database import db
from celebrities import CELEBRITIES_DATABASE

def migrate_celebrities():
    """Migrate celebrity data from dictionary to database"""
    print("Starting celebrity data migration...")
    
    total_celebrities = 0
    successful_migrations = 0
    
    for category, celebrities in CELEBRITIES_DATABASE.items():
        print(f"Migrating {len(celebrities)} celebrities from {category} category...")
        
        for celebrity in celebrities:
            total_celebrities += 1
            
            # Ensure the celebrity has all required fields
            celebrity_data = {
                'id': celebrity['id'],
                'name': celebrity['name'],
                'image': celebrity.get('image', ''),
                'bio': celebrity.get('bio', ''),
                'voice_sample': celebrity.get('voice_sample', ''),
                'languages': celebrity.get('languages', []),
                'popularity': celebrity.get('popularity', 0),
                'debut_year': celebrity.get('debut_year', 0),
                'notable_films': celebrity.get('notable_films', []),
                'voice_characteristics': celebrity.get('voice_characteristics', []),
                'category': celebrity.get('category', category)
            }
            
            if db.insert_celebrity(celebrity_data):
                successful_migrations += 1
                print(f"✓ Migrated: {celebrity['name']}")
            else:
                print(f"✗ Failed to migrate: {celebrity['name']}")
    
    print(f"\nMigration completed!")
    print(f"Total celebrities: {total_celebrities}")
    print(f"Successfully migrated: {successful_migrations}")
    print(f"Failed migrations: {total_celebrities - successful_migrations}")

def verify_migration():
    """Verify that the migration was successful"""
    print("\nVerifying migration...")
    
    # Check total count
    all_celebrities = db.get_all_celebrities()
    print(f"Total celebrities in database: {len(all_celebrities)}")
    
    # Check categories
    categories = db.get_categories()
    print(f"Categories in database: {categories}")
    
    # Check each category
    for category in categories:
        category_celebrities = db.get_celebrities_by_category(category)
        print(f"  {category}: {len(category_celebrities)} celebrities")
    
    # Test search functionality
    search_results = db.search_celebrities("Khan")
    print(f"Search results for 'Khan': {len(search_results)} celebrities")
    
    print("Migration verification completed!")

if __name__ == "__main__":
    # Run migration
    migrate_celebrities()
    
    # Verify migration
    verify_migration()
    
    print("\nDatabase migration completed successfully!")
    print("You can now use the new database-based celebrity system.")
