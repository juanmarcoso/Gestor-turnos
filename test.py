from services.category_service import CategoryService
from services.provider_service import ProviderService

category_service = CategoryService()
provider_service = ProviderService()

# Example flow
categories = category_service.list_categories()
print("📂 Categories:")
for i, category in enumerate(categories):
    print(f"{i + 1}. {category.name}")

cat_choice = int(input("Select a category: ")) - 1
selected_category = categories[cat_choice]

providers = provider_service.list_providers_by_category(selected_category.id)
print(f"\n👨‍⚕️ Providers in {selected_category.name}:")
for i, provider in enumerate(providers):
    print(f"{i + 1}. {provider.name}")
