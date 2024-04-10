import requests
from bs4 import BeautifulSoup

# List of websites to check
websites = [
    'https://www.yourweb-site.com',
    'https:myweb.com',

]


# Initialize lists to keep track of websites with and without Yoast SEO
websites_with_yoast = []
websites_without_yoast = []

for website in websites:
    try:
        response = requests.get(website)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Check for 'yoast.com' phrase to determine if Yoast SEO is installed
        if 'yoast.com' in str(soup):
            websites_with_yoast.append(website)
        else:
            websites_without_yoast.append(website)
    except Exception as e:
        print(f'Error checking {website}: {e}')

# Print the lists
print("Websites with Yoast SEO:")
for website in websites_with_yoast:
    print(website)

print("\nWebsites without Yoast SEO:")
for website in websites_without_yoast:
    print(website)
