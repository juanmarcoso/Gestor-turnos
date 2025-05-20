from services.category_service import CategoryService
from services.provider_service import ProviderService
from services.appointment_service import AppointmentService
from notifier.confirmation_service import ConfirmationService
from db.conexion import *

def main():
    conectar()
    category_service = CategoryService()
    provider_service = ProviderService()
    appointment_service = AppointmentService()

    while True:
        # Step 1: Select category
        categories = category_service.list_categories()
        print("\n📂 Categories:")
        for i, category in enumerate(categories):
            print(f"{i + 1}. {category.name}")

        try:
            category_option = int(input("\nSelect a category (0 to exit): "))
            if category_option == 0:
                break
            selected_category = categories[category_option - 1]
        except (ValueError, IndexError):
            print("❌ Invalid category option.")
            continue

        # Step 2: Select provider
        providers = provider_service.list_providers_by_category(selected_category.id)
        if not providers:
            print("⚠️ No providers available in this category.")
            continue

        print(f"\n👨‍⚕️ Providers in {selected_category.name}:")
        for i, provider in enumerate(providers):
            print(f"{i + 1}. {provider.name}")

        try:
            provider_option = int(input("\nSelect a provider (0 to go back): "))
            if provider_option == 0:
                continue
            selected_provider = providers[provider_option - 1]
        except (ValueError, IndexError):
            print("❌ Invalid provider option.")
            continue

        # Step 3: Show appointments for selected provider
        appointments = appointment_service.list_appointments_for_provider(selected_provider.id)
        if not appointments:
            print("⏳ No available appointments for this provider.")
            continue

        print(f"\n📅 Available Appointments for {selected_provider.name}:")
        for i, appointment in enumerate(appointments):
            print(f"{i + 1}. {appointment}")

        try:
            appointment_option = int(input("\nSelect an appointment (0 to go back): "))
            if appointment_option == 0:
                continue
            booked = appointment_service.book_appointment_by_provider(selected_provider.id, appointment_option - 1)
            if booked:
                ConfirmationService.confirm(booked)
            else:
                print("❌ Invalid appointment option.")
        except ValueError:
            print("❌ Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
