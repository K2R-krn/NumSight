import os
import random
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.db import models
from core.models import GlobalUser, GlobalContacts
from faker import Faker
import phonenumbers
from phonenumbers import PhoneNumberFormat
import random

def generate_random_phone():
    """Generate a random phone number in E.164 format"""
    fake = Faker()
    phone_obj = phonenumbers.parse(fake.phone_number(), "US")
    return phonenumbers.format_number(phone_obj, PhoneNumberFormat.E164)

def populate_global_users(num_users=100):
    """Create dummy GlobalUser entries"""
    fake = Faker()
    
    print(f"Creating {num_users} GlobalUser records...")
    
    existing_phones = []
    
    for _ in range(num_users):
    
        while True:
            phone = generate_random_phone()
            if phone not in existing_phones:
                existing_phones.append(phone)
                break
        
    
        has_name = random.random() > 0 
        has_email = random.random() > 0  
        
        total_appearance = random.randint(1, 50)
        num_spam = random.randint(0, total_appearance)
        
        
        if total_appearance > 0:
            spam_likelihood = int((num_spam / total_appearance) * 100)
        else:
            spam_likelihood = 0
            
        
        user = GlobalUser(
            name=fake.name() if has_name else None,
            phone_number=phone,
            email_address=fake.email() if has_email else None,
            num_spam=num_spam,
            total_appearance=total_appearance,
            spam_likelyhood=spam_likelihood  
        )
        user.save()
    
    print(f"Created {num_users} GlobalUser records successfully!")

def populate_global_contacts(num_contacts=200):
    """Create dummy GlobalContacts entries using emails from GlobalUser"""
    print(f"Creating up to {num_contacts} GlobalContacts records...")
    
    users_with_email = list(GlobalUser.objects.exclude(email_address=None).values_list('email_address', flat=True))
    
    if len(users_with_email) < 2:
        print("Not enough users with email addresses to create contacts. Please add more users with emails.")
        return
    
    contacts_created = 0
    
    for from_email in users_with_email:
        num_user_contacts = random.randint(1, min(10, len(users_with_email) - 1))
    
        potential_recipients = [email for email in users_with_email if email != from_email]
        
        to_emails = random.sample(potential_recipients, min(num_user_contacts, len(potential_recipients)))
        
        for to_email in to_emails:
            contact = GlobalContacts(
                contact_from=from_email,
                contact_to=to_email
            )
            contact.save()
            contacts_created += 1
            
            if contacts_created >= num_contacts:
                break
                
        if contacts_created >= num_contacts:
            break
    
    print(f"Created {contacts_created} GlobalContacts records successfully!")

def run():
    """Main function to run the script"""
    confirm = input("Would you like to clear existing data before populating? (yes/no): ")
    if confirm.lower() == 'yes':
        GlobalUser.objects.all().delete()
        GlobalContacts.objects.all().delete()
        print("Existing data cleared!")
    
    try:
        num_users = int(input("How many GlobalUser records would you like to create? (default: 100): ") or 100)
        num_contacts = int(input("How many GlobalContacts records would you like to create? (default: 200): ") or 200)
    except ValueError:
        print("Invalid input. Using default values.")
        num_users = 100
        num_contacts = 200
    
    populate_global_users(num_users)
    populate_global_contacts(num_contacts)
    
    print("Data population complete!")

if __name__ == "__main__":
    run()