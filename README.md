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

* To add, edit and delete products with the relevant information (price, description, rating, comments, image, sizes and category) on the website.
* To allow a user make a purchase of the products on the website.
* To categorise sale items on the website.

The primary goal of the website from a site users perspective is as follows:

* To register for an account on the website and receive an email after successful registration.
* To login or logout from the website.
* To easily recover my password in case I forget it.
* Have a personalised user profile with my delivery, payment information and order history.
* View a list of products on the website.
* View an individual product detail(price, description, rating, comments, image, sizes and category)
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
* Products (part of the original Boutique Ado project): This app contains functionality regarding a product. I added functionality for adding/removing a rating/comment to a product
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
 


