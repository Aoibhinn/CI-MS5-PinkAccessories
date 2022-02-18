## Manual testing information

### Feature 1 Navigation Bar and Homepage
#### User Stories feature 1
1. Navigate to https://ci-ms5-pinkaccessories.herokuapp.com, and click on the My Account link as a regular user
2. Login to the website with a valid username and password, and click on the My Account link
3. Navigate to the "All Products" filter, and then click By Price
4. Navigate to the "All Products" filter, and then click By Rating
5. Navigate to the "All Products" filter, and then click By Category
6. Navigate to the "Necklaces" filter, and filter by Necklaces
7. Navigate to the "Earrings" filter, and filter by Earrings
8. Navigate to the "Bracelets" filter, and filter by Bracelets
9. Navigate to the "Scarves" filter, and filter by Bracelets
10. Navigate to the "Hats" filter, and filter by Bracelets
11. Navigate to the "Fascinators" filter, and filter by Fascinators
12. Navigate to the "Totes" filter, and filter by Totes
13. Navigate to the "Clutchs" filter, and filter by Bracelets
14. Click the Logout link under My profile and logout
15. Login as an admin user

#### User Story Testing Results 1
Step| Result | Desktop | Tablet | Mobile | Status
------------ | ------------ | ------------- | ------------- | ------------- | -------------
Step 1 | The homepage is displayed, Login and Register links are displayed under My Account and the footer items are displayed with website links(Register/Login) | [Desktop](readme/testing/homepage_notloggedin_desktop.png)  | [Tablet](readme/testing/homepage_notloggedin_ipad.png)  | [Mobile](readme/testing/homepage_notloggedin_iphone.png)  | Passed |
Step 2 | The homepage is displayed with a header logo(desktop), search box(expands on tablet/mobile), My account, Favourites and shopping bag icons. My Profile/Logout is visible under My Account and the footer contains links for My Profile, News and Sale   | [Desktop](readme/testing/homepage_loggedin_desktop.png) | [Tablet](readme/testing/homepage_notloggedin_ipad.png)  | [Mobile](readme/testing/homepage_loggedin_iphone.png) | Passed |
Step 3 | Products on the page are filtered by Price (Low-High) | [Desktop](readme/testing/products_filterpricelow_desktop.png) | [Tablet](readme/testing/products_filterpricelow_ipad.png)  | [Mobile](readme/testing/products_filterpricelow_iphone.png)  | Passed |
Step 4 | Products on the page are filtered by Rating (High-Low) | [Desktop](readme/testing/products_filterpricehigh_desktop.png)  | [Tablet](readme/testing/products_filterpricehigh_ipad.png) | [Mobile](readme/testing/products_filterpricehigh_iphone.png)  | Passed |
Step 5 | Products on the page are filtered by Category (A-Z) | [Desktop](readme/testing/products_filterA_Z_desktop.png)  | [Tablet](readme/testing/products_filterA_Z_ipad.png)  | [Mobile](readme/testing/products_filterA_Z_iphone.png) | Passed  |
Step 6 | Products on the page are filtered by Necklaces | [Desktop](readme/testing/category_necklace_desktop.png) | [Tablet](readme/testing/category_necklace_ipad.png)  | [Mobile](readme/testing/category_necklace_iphone.png) | Passed  |
Step 7 | Products on the page are filtered by Earrings | [Desktop](readme/testing/category_earrings_desktop.png)  | [Tablet](readme/testing/category_earrings_ipad.png)  | [Mobile](readme/testing/category_earrings_iphone.png)  | Passed |
Step 8 | Products on the page are filtered by Bracelets | [Desktop](readme/testing/category_bracelets_desktop.png)| [Tablet](readme/testing/category_bracelets_ipad.png)  | [Mobile](readme/testing/category_bracelets_iphone.png)  | Passed |
Step 9 | Products on the page are filtered by Scarves | [Desktop](readme/testing/category_scarves_desktop.png) | [Tablet](readme/testing/category_scarves_ipad.png) | [Mobile](readme/testing/category_scarves_iphone.png)  | Passed |
Step 10 | Products on the page are filtered by Hats | [Desktop](readme/testing/category_scarves_desktop.png) | [Tablet](readme/testing/category_scarves_ipad.png)  | [Mobile](readme/testing/category_scarves_iphone.png)  | Passed |
Step 11 | Products on the page are filtered by Facinators | [Desktop](readme/testing/category_fascinator_desktop.png) | [Tablet](readme/testing/category_fascinator_ipad.png)  | [Mobile](readme/testing/category_fascinator_iphone.png) | Passed |
Step 12 | Products on the page are filtered by Totes | [Desktop](readme/testing/category_tote_desktop.png) | [Tablet](readme/testing/category_tote_ipad.png)  | [Mobile](readme/testing/category_tote_iphone.png) | Passed |
Step 13 | Products on the page are filtered by Clutchs | [Desktop](readme/testing/category_clutch_desktop.png) | [Tablet](readme/testing/category_clutch_ipad.png) | [Mobile](readme/testing/category_clutch_iphone.png)  | Passed |
Step 14 | The user is logged out | [Desktop](readme/testing/loggingout_desktop.png)  | [Tablet](readme/testing/loggingout_ipad.png)  | [Mobile](/workspace/CI-MS5-PinkAccessories/readme/testing/loggingout_iphone.png) | Passed |
Step 15 | The homepage is displayed with a header logo(desktop), search box(expands on tablet/mobile), My Account and shopping bag icons. Product Management/News Item Management/My Profile/Logout is visible under My Account and the footer contains links for Product Management  | [Desktop](readme/testing/homepage_admin_desktop.png)  | [Tablet](readme/testing/homepage_admin_ipad.png)  | [Mobile](readme/testing/homepage_admin_iphone.png)  | Passed |


#### User Stories Steps 2
1. As a regular user scroll down to the footer on the homepage 
2. As an admin user scroll down to the footer on the homepage
3. As a regular user sign up to the newsletter

#### User Story Testing Results 2
Step| Result | Desktop | Tablet | Mobile | Status
------------ | ------------ | ------------- | ------------- | ------------- | -------------
Step 1 | The footer items are displayed with website link(Profile) | [Desktop]  | [Tablet]  | [Mobile]  |  |
Step 2 | The footer items are displayed with website links(Product Management | [Desktop]  | [Tablet] | [Mobile]  |  |
Step 3 | The user receives an email | [Desktop] | [Tablet]  | [Mobile]  |  |

### Feature 3 Register
#### User Stories feature 3
- User Story 3.1: As a regular user I can register on the website by providing an email address, email address(confirmation), username, password, password confirmation
- User Story 3.1: As a regular user I will receive an email to verify my account after registering
- User Story 3.1: As a regular user I can log in to my account once I click on the verification link in the email I receive regarding my registration

#### User Stories Steps 3
1. As a regular user, navigate to the registration page, fill in email address, email address(confirmation), username, password, password confirmation and click Sign Up
2. Open the email received
3. Click on the verification link in the email received
4. Confirm the email address for the account
5. Sign in to the account
6. Attempt to register with the same account and do not fill in all the mandatory fields: email address, email address(confirmation), username, password, password confirmation

#### User Story Testing Results 3
Step| Result | Desktop | Tablet | Mobile | Status
------------ | ------------ | ------------- | ------------- | ------------- | -------------
Step 1 | The user registers for an account | [Desktop](readme/testing/register_desktop.png)  | [Tablet](readme/testing/register_ipad.png)  | [Mobile](readme/testing/register_iphone.png)  | Passed  |
Step 2 | The user receives the email | [Desktop](readme/testing/verifyemail_desktop.png)  | [Tablet](readme/testing/verifyemail_ipad.png)  | [Mobile](readme/testing/verifyemail_iphone.png)  | Passed  |
Step 3 | The user clicks on the verification link | [Desktop](readme/testing/confirmemail_desktop.png) | [Tablet](readme/testing/confirmemail_ipad.png) | [Mobile](readme/testing/confirmemail_iphone.png)  | Passed  |
Step 4 | The user confirms the email address | [Desktop](readme/testing/emailedconfirmed_desktop.png)  | [Tablet](readme/testing/emailedconfirmed_ipad.png)  | [Mobile](readme/testing/emailedconfirmed_iphone.png) | Passed  |
Step 5 | The user logs in to the site | [Desktop](readme/testing/successfullysignedin_desktop.png)  | [Tablet](readme/testing/successfullysignedin_ipad.png)  | [Mobile](readme/testing/successfullysignedin_iphone.png) | Passed  |
Step 6 | A message is displayed to the user | [Desktop](readme/testing/fiedsrequired_desktop.png) | [Tablet](readme/testing/fieldsrequired_ipad.png) | [Mobile](readme/testing/fieldsrequired_iphone.png)  | Passed  | 

### Feature 4 Login
#### User Stories feature 4
- User Story 4.1: As an admin/regular user I can log in to the website using my username or email address and password. Both fields are mandatory. Once correct, I will be navigated to the homepage and a message displayed
- User Story 4.2: As an admin/regular user I can request a new password if I forget my current password. I will receive an email to reset my password. Once I reset I can log in
#### User Stories Steps 4
1. Attempt to log in to the website with an account that does not exist or an incorrect password
2. Request a new password
3. Login to the site with the correct account details
#### User Story Testing Results 4
Step| Result | Desktop | Tablet | Mobile | Status
------------ | ------------ | ------------- | ------------- | ------------- | -------------
Step 1 | A message is displayed to the user | [Desktop](readme/testing/loginfails_desktop.png)  | [Tablet](readme/testing/loginfails_ipad.png)  | [Mobile](readme/testing/loginfails_iphone.png)  | Passed |
Step 2 | The user receives an email where they can reset their password | [Desktop](readme/testing/password_reset_email.png)  |  |  | Passed |
Step 3 | The user can successfully log in | [Desktop](readme/testing/password_updated_desktop.png)  | [Tablet](readme/testing/password_updated_ipad.png)  | [Mobile](readme/testing/password_updated_iphone.png)  | Passed |

### Feature 5 Products and Product Detail Pages
#### User Stories feature 5
- User Story 5.1: As a regular user I can view the products page with product count and with each product image, title, category, price and presale price(if applicable)
- User Story 5.2: As a regular user I can sort the products by Price(high to low, low to high), Rating(high to low, low to high), Name(A-Z, Z-A), Category(A-Z, Z-A)
- User Story 5.3: As a regular user if I click on a product I will be navigated to the product detail page
- User Story 5.4: As a regular user I can view the product image, description, colour, code, rating, category, description
- User Story 5.5: As a regular user I can click on the Keep Shopping button on the product detail page, and it will navigate the user to the products page
- User Story 5.6: As a regular user I can set the product size(if applicable for the product) and quantity for a product (one plus)
- User Story 5.7: As an admin user I can view the Add product page by clicking on the Product Management link.
- User Story 5.8: As an admin user I can view the Edit product page by clicking on the Edit button on the product. 
- User Story 5.9: As an admin user I can click on a product, and I am navigated to the product detail page. I can edit or delete the product by clicking on the Edit or Delete links on the page

#### User Stories Steps 5
1. As a regular user login to the website and navigate to the products page
2. Sort the products from Price(High to Low)
3. Click on a product
4. Add a product(bags) to the bag, with a quantity of 2
5. As an admin user login and click on the add product(Product Management)
6. Click on the edit button on the products page or in the product detail page and edit the product
7. As an admin user delete a product


#### User Story Testing Results 5
Step| Result | Desktop | Tablet | Mobile | Status
------------ | ------------ | ------------- | ------------- | ------------- | -------------
Step 1 | The products page is displayed | [Desktop](readme/testing/products_desktop.png)  | [Tablet](readme/testing/products_ipad.png)  | [Mobile](readme/testing/products_iphone.png)  | Passed |
Step 2 | The products are sorted High to Low | [Desktop](readme/testing/product_price_desktop.png)  | [Tablet](readme/testing/product_price_ipad.png)  | [Mobile](readme/testing/product_price_iphone.png)  | Passed |
Step 3 | The product detail is displayed | [Desktop](readme/testing/product_detail_desktop.png)  | [Tablet](readme/testing/product_detail_ipad.png)  | [Mobile](readme/testing/product_detail_iphone.png)  | Passed |
Step 4 | The 2 products are added | [Desktop](readme/testing/add_bad_to_cart_desktop.png)  | [Tablet](readme/testing/add_bad_to_cart_ipad.png)  | [Mobile](readme/testing/add_bad_to_cart_iphone.png)  | Passed |
Step 5 | The add product page is displayed | [Desktop](readme/testing/add_product_desktop.png)  | [Tablet](readme/testing/add_product_ipad.png)  | [Mobile](readme/testing/add_product_iphone.png)  | Passed |
Step 6 | The edit product page is displayed | [Desktop](readme/testing/10_2_1_desktop.PNG)  | [Tablet](readme/testing/delete_product_ipad.png)  | [Mobile](readme/testing/10_2_1_mobile.PNG)  | Passed |
Step 7 | Delete a product notification displayed | [Desktop](readme/testing/delete_product_desktop.png)  | [Tablet](readme/testing/delete_product_ipad.png)  | [Mobile](readme/testing/delete_product_iphone.png)  | Passed |

### Feature 6 Profile Page
#### User Stories feature 6
- User Story 9.1: As a regular user I can view my Default delivery information: Phone Number, Street Address 1, Street Address 2, Town or City, County, State or Locality, Postal Code and Country
- User Story 9.2: As a regular user I can update my Default delivery information: Phone Number, Street Address 1, Street Address 2, Town or City, County, State or Locality, Postal Code and Country
- User Story 9.3: As a regular user I can view my order history(Order Number, Date, Items and Order Total)
- User Story 9.4: As a regular user I can click on an order number to view the order information (Order number, Order date/time, Full Name, Street Address 1, Street Address 2, Town or City, County, State or Locality, Postal Code and Country, Phone Number, Order Total, Deliver, Grand Total)

#### User Stories Steps 6
1. Click on the My Profile link under My Account
2. Update one field in the default delivery information (Street Address 2)
3. Click on an order number

#### User Story Testing Results 6
Step | Result | Desktop | Tablet | Mobile | Status
------------ | ------------ | ------------- | ------------- | ------------- | -------------
Step 1 | The users default delivery information and order history is displayed  | [Desktop](readme/testing/shopper_profile_desktop.png)  | [Tablet](readme/testing/shopper_profile_ipad.png)  | [Mobile](readme/testing/shopper_profile_iphone.png)  | Passed |
Step 2 | The users default delivery information is updated and displayed (Street Address 1)  | [Desktop](readme/testing/profile_update_desktop.png)  | [Tablet](readme/testing/profile_update_ipad.png)  | [Mobile](readme/testing/profile_update_iphone.png)  | Passed |
Step 3 | The users order details is displayed | [Desktop](readme/testing/order_history_desktop.PNG)  | [Tablet](readme/testing/order_history_tablet.PNG)  | [Mobile](readme/testing/order_history_mobile.PNG)  | Passed |



