'Pink Accessories' is a fabulous ecommerce website allowing users purchase jewellery, bags hats and scarves developed for developed for Milestone 5 project 5 as part of the Code Institute - Diploma in Software Development (Full stack) course.

There are two types of users, and I have set up accounts for both
* An admin(administrator) user account has been set up with username/password of admin/Password1@
* A regular(shopper) user account has been set up with username/password of (Add login for shopper)
* When making a payment as a regular user, a test credit card of 4242424242424242 has been set up for the card number.
* For the expiry date, cvc and postal code any series number(s) can be used(once they meet the mimimum values).

View the live site (Link to Live Site)

# Project Overview
* This project is a website is for submission as milestone project 5 as part of the Code Institute - Diploma in Software * Development (Full stack) course.
* The website is deployed using Heroku pages at the following url: (Link to heroku)
* The repository on GitHub that contains the website source code and assets is available at the following url: (Link to code repository )
* The website was built with a responsive look and feel for desktop, tablet and mobile devices.

# UX
## Strategy
The primary goal of the website from the site owners perspective is as follows:

* To add, edit and delete products with the relevant information (price, description, image, sizes and category) on the website.
* To allow a user make a purchase of the products on the website.
* To categorise sale items on the website.

The primary goal of the website from a site users perspective is as follows:

* To register for an account on the website and receive an email after successful registration.
* To login or logout from the website.
* To easily recover my password in case I forget it.
* Have a personalised user profile with my delivery, payment information and order history.
* View a list of products on the website.
* View an individual product detail(price, description, rating,image, sizes and category)
* To add an item to a shopping bag, and select the quantity and size if applicable
* Complete a purchase of items in a shopping bag.
* To sort the list of available products by rating, price and category.
* Search for a product by name or description and view the search results.

# Structure
## Website pages
* I used the Bootstrap grid system throughout, which gave a consistent structure and responsive design "out of the box".
* Below are the main page's/features functionality wise, there are some others for password reset/verification etc. that are described in the user story section.
* All pages have a common look and feel and a common header/footer. On a tablet/mobile the look and feel is slightly different with a burger menu.
* These pages are described in more detail in the user stories section.

Page            |Description
:-------------         |:------------- 
Home     | 
Products           |     
Product Detail           | The product detail page displays the product image, description, price, add to bag buttons    
Product Management(Add Product)     | A product can be added to the website    
Product Management(Edit Product)     | A product can be edited to the website     
Product Management(Delete Product)     | A product can be deleted from the website. This is a modal triggered by a delete button
My Profile             |The users profile(delivery information) and previous orders is displayed       
Order History         | A order history page per order details the order information and price
Log out               | A logout button is provided under the My Account link to logout
Register               | A user can register an account on the site with a valid email address
Log in               | A user can login with a valid username and password         
Bag | A user can add products to a shopping bag which contains each item in the order and an overall price/delivery if applicable   
Checkout | A user can enter their delivery details and credit card information to checkout an order   
Checkout success | Once an order is successful, the user can view the checkout success


## Code Structure
The project is divided into a number of apps, as is built using the Django Framework.
The project was built on the Boutique Ado project, that was part of the project content.
The apps are described as follows:

* Bag (part of the original Boutique Ado project): This app contains functionality regarding a users shopping bag
* Checkout (part of the original Boutique Ado project): This app contains functionality regarding a users checking out and payment of an order
* Home (part of the original Boutique Ado project): This app contains functionality regarding the users home page
* Products (part of the original Boutique Ado project): This app contains functionality regarding a product. 
* Profiles (part of the original Boutique Ado project): This app contains functionality regarding a users profile and order history 

To complement the apps there are:

- pink_accessories : Containing settings.py(Settings) and urls.py(Website urls) for example
- templates: Containing the base.html, allauth(django authentication) and includes html files
- static: Base css and Javascript files(toast and send_email) There is some javascript in some html files, but I have tried to minimise that
- manage.py: Main python file for starting the website
- README.md: Readme documentation
- custom_storage.py: AWS Boto3 configuration
- Procfile: To run the application
- Requirements.txt: Containing the python libraries installed
Note: Environment variable values are not exposed in the source code, they are stored locally in env.py that is not checked in(and listed in .gitignore, and on Heroku in app settings)

#### Models
- The following models were created to represent the database model structure for the website
##### User Model
- The User model contains information about the user. It is part of the Django allauth library
- The model contains the following fields: username, password, first_name, last_name, email, is_staff, is_active, is_superuser, last_login, date_joined

##### User Model
- The User model has a one-to-one relationship with User
- The model contains the following fields: default_phone_number, default_street_address1, default_street_address2
default_town_or_city, default_county, default_postcode and default_country

##### Order Model
- The Order model contains information about orders made on the website.
- It contains UserProfile as a foreign-key.
- The model contains the following fields: order_number, user_profile, full_name, email, phone_number, country, postcode, town_or_city, street_address1, street_address2, county, date, delivery_cost, order_total, grand_total, original_bag, stripe_pid

##### OrderLineItem Model
- The OrderLineItem model contains information about an entry in an order, for orders made on the website.
- It contains Order and Product as foreign-keys.
- The model contains the following fields: order, product, product_size, quantity, lineitem_total

##### Product Model
- The Product Model represents a product and its details
- It contains Category as a foreign-key
- The model contains the following fields: name, category, price, colour, code, description, has_sizes, rating, pre_sale_price, image_url, image
- The image field contains the product image
- The image_url field contains the url to where the image file is physically stored, for example AWS S3 bucket

##### Category Model
- The Category model contains a product category
- The model contains the following fields: name, friendly_name

## Scope
### User Stories Potential or Existing Customer

The user stories for the regular user eg: "shopper user" (a potential or existing customer) are described as follows: 

- User Story 1.1: As an admin/regular user the navigation bar is displayed with a logo on all pages with a search box, My account, and shopping bag icons on a desktop device
- User Story 1.2: As an admin/regular user the navigation bar is displayed on all pages with a search box, My account, and shopping bag icons on a mobile/tablet device
- User Story 1.3: As a regular user not logged in, I see a Register/Login link under the My Account dropdown
- User Story 1.6: As a regular user logged in/not logged in, I am brought to my shopping bag if I click on the Bag icon
- User Story 1.7: As a regular/admin user logged in, I see a "My Profile"/Logout under the My Account dropdown
- User Story 1.9: As a regular/admin user logged in, if I click on the My Profile under My Account I am brought to the My Profile page
- User Story 1.10: As a regular/admin user logged in, if I click on the My Profile under My Account I am brought to the Logout page. If I click Logout I am Logged out. If I click cancel I am brought back to the homepage
- User Story 1.13: As a regular/admin user I can view the Home link in the header, and clicking it will bring the user to the homepage
- User Story 1.15: As a regular/admin user I can click on the "All Products" filter, click By Price, and will be brought to the Products page, with products price low to high displayed
- User Story 1.16: As a regular/admin user I can click on the "All Products" filter, click By Rating, and will be brought to the Products page, with products rating high to low displayed
- User Story 1.17: As a regular/admin user I can click on the "All Products" filter, click By Category, and will be brought to the Products page, with products category a-z displayed
- User Story 1.18: As a regular/admin user I can click on the "Jewellery" filter, and filter by Necklaces, Bracelets, Earrings or All Jewellery
- User Story 1.19: As a regular/admin user I can click on the "Bags" filter, and filter by Clutchs, Totes, or All Bags
- User Story 1.20: As a regular/admin user I can click on the "Hats & Scarves" filter, and filter by Scarves, Hats, Fascinators All Hats & Scarves
- User Story 2.2: As a regular user the footer is displayed with a logo, product links(Jewellery, Bags, Scarves & Hats), website link(Profile)
- User Story 2.4: As a regular user I can sign up for a newsletter by entering my email address and clicking Signup. I will receive an email after signing up
- User Story 3.1: As a regular user I can register on the website by providing an email address, email address(confirmation), username, password, password confirmation
- User Story 3.1: As a regular user I will receive an email to verify my account after registering
- User Story 3.1: As a regular user I can log in to my account once I click on the verification link in the email I receive regarding my registration
- User Story 4.1: As an admin/regular user I can log in to the website using my username or email address and password. Both fields are mandatory. Once correct, I will be navigated to the homepage and a message displayed
- User Story 4.2: As an admin/regular user I can request a new password if I forget my current password. I will receive an email to reset my password. Once I reset I can log in
- User Story 5.1: As a regular user I can view the products page with product count and with each product image, title, category, price and presale price(if applicable)
- User Story 5.2: As a regular user I can sort the products by Price(high to low, low to high), Rating(high to low, low to high), Name(A-Z, Z-A), Category(A-Z, Z-A)
- User Story 5.4: As a regular user if I click on a product I will be navigated to the product detail page
- User Story 5.5: As a regular user I can view the product image, description, colour, code, rating, category and description
- User Story 5.11: As a regular user I can set the product size(if applicable for the product) and quantity for a product (one plus)
- User Story 6.1: As a regular user I can view the products with product image, category, and price is displayed
- User Story 9.1: As a regular user I can view my Default delivery information: Phone Number, Street Address 1, Street Address 2, Town or City, County, State or Locality, Postal Code and Country
- User Story 9.2: As a regular user I can update my Default delivery information: Phone Number, Street Address 1, Street Address 2, Town or City, County, State or Locality, Postal Code and Country
- User Story 9.3: As a regular user I can view my order history(Order Number, Date, Items and Order Total)
- User Story 9.4: As a regular user I can click on an order number to view the order information (Order number, Order date/time, Full Name, Street Address 1, Street Address 2, Town or City, County, State or Locality, Postal Code and Country, Phone Number, Order Total, Deliver, Grand Total)
- User Story 12.1: As a regular user I can click on a product, set the size(if applicable) and quantity, click Add to Bag and the product will be added to my bag, a message displayed, and a toast will be displayed with the bag contents
- User Story 12.2: As a regular user I can click on the bag icon, I will be brought to my bag. If there are no items in the bag, a message will be displayed
- User Story 12.3: As a regular user I can click on the bag icon, I will be brought to my bag. If there are items, the product image, detail, price, quantity, subtotal will be displayed for the item. The bag total, delivery(if applicable), grand total would be displayed
- User Story 12.4: As a regular user I can update the quantity or remove an item from my shopping bag
- User Story 12.5: As a regular user I can click on the Secure Checkout button on the bag page or toast message, and I will be brought to the Checkout page
- User Story 12.6: As a regular user on the checkout page I can set my details(Full Name, email address, both mandatory) and Delivery Information(Phone Number(mandatory), Street Address 1(mandatory), Street Address 2, Town or City(mandatory, County, State or Locality, Postal Code and Country(mandatory), which is populated from my profile if filled in
- User Story 12.7: As a regular user on the checkout page I can view the order summary(item image, title, size, quantity, subtotal, order total, delivery, grand total)
- User Story 12.8: As a regular user on the checkout page if the order total is greater than 99 euros, there is no delivery charge
- User Story 12.9: As a regular user on the checkout page if the order total is less than 99 euros, there is delivery charge(10% of the order total) A message is displayed to the user on the toast message of what they need to add to the bag to avail of no delivery charge
- User Story 12.10: As a regular user on the checkout page if I click "Save this delivery information to my profile", the details entered will be saved on the users profile
- User Story 12.11: As a regular user on the checkout page I can enter a credit card number(16 digits), expiry date(2 digits/2digits) and a postal code(up to 5 digits), these fields are mandatory
- User Story 12.12: As a regular user on the checkout page if I click the Keep Shopping button I will be navigated to the products page
- User Story 12.13: As a regular user on the checkout page if I click the Complete Order button, and the transaction is not successful, a message will be displayed
- User Story 12.14: As a regular user on the checkout page if I click the Complete Order button, and the transaction is successful, the user will be navigated to a checkout success page, and an email is sent to the user
- User Story 12.15: As a regular user on the checkout page if I click the Complete Order button, and the transaction is successful, the order is saved to my order history in My profile page
- User Story 12.16: As a regular user on the checkout success page, the Order details will be displayed (Order number, Order date/time, Full NameStreet Address 1, Street Address 2, Town or City, County, State or Locality, Postal Code and Country, Phone Number, Order Total, Deliver, Grand Total) and a link to the sales item page is displayed
- User Story 12.17: As a regular user not logged in, I can add items to my bag and make a purchase

 


