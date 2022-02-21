# Table of Contents
- [Testing](#testing)
  * [Manual testing information](#manual-testing-information)
    + [Feature 1 Navigation Bar and Homepage](#feature-1-navigation-bar-and-homepage)
      - [User Stories Steps 1](#user-stories-steps-1)
      - [User Story Testing Results 1](#user-story-testing-results-1)
    + [Feature 2 Footer](#feature-2-footer)
      - [User Stories Steps 2](#user-stories-steps-2)
      - [User Story Testing Results 2](#user-story-testing-results-2)
    + [Feature 3 Register](#feature-3-register)
      - [User Stories feature 3](#user-stories-feature-3)
      - [User Stories Steps 3](#user-stories-steps-3)
      - [User Story Testing Results 3](#user-story-testing-results-3)
    + [Feature 4 Login](#feature-4-login)
      - [User Stories feature 4](#user-stories-feature-4)
      - [User Stories Steps 4](#user-stories-steps-4)
      - [User Story Testing Results 4](#user-story-testing-results-4)
    + [Feature 5 Products and Product Detail Pages](#feature-5-products-and-product-detail-pages)
      - [User Stories feature 5](#user-stories-feature-5)
      - [User Stories Steps 5](#user-stories-steps-5)
      - [User Story Testing Results 5](#user-story-testing-results-5)
    + [Feature 6 Profile Page](#feature-6-profile-page)
      - [User Stories feature 6](#user-stories-feature-6)
      - [User Stories Steps 6](#user-stories-steps-6)
      - [User Story Testing Results 6](#user-story-testing-results-6)
    + [Feature 07 Product Management](#feature-07-product-management)
      - [User Story 07-1](#user-story-07-1)
      - [User Story Steps 07-1](#user-story-steps-07-1)
      - [User Story Testing Results 07-1](#user-story-testing-results-07-1)
      - [User Story 07-2](#user-story-07-2)
      - [User Story Steps 07-2](#user-story-steps-07-2)
      - [User Story Testing Results 07-2](#user-story-testing-results-07-2)
      - [User Story 07-3](#user-story-07-3)
      - [User Story Steps 07-3](#user-story-steps-07-3)
      - [User Story Testing Results 07-3](#user-story-testing-results-07-3)
    + [Feature 08 shopping bag](#feature-08-shopping-bag)
      - [User Stories feature 08](#user-stories-feature-08)
      - [User Stories Steps 08](#user-stories-steps-08)
      - [User Story Testing Results 08](#user-story-testing-results-08)
    + [Feature 9 Admin](#feature-9-admin)
      - [User Story 9-1](#user-story-9-1)
      - [User Story Steps 9-1](#user-story-steps-9-1)
      - [User Story Testing Results 9-1](#user-story-testing-results-9-1)
      - [User Story 9-2](#user-story-9-2)
      - [User Story Steps 9-2](#user-story-steps-9-2)
      - [User Story Testing Results 9-2](#user-story-testing-results-9-2)
      - [User Story 9-3](#user-story-9-3)
      - [User Story Steps 13-3](#user-story-steps-9-3)
      - [User Story Testing Results 9-10](#user-story-testing-results-9-10)

## Manual testing information
Testing was completed on the following browsers and device types

Device Number | Physical/Emulator | Device Name | Device Type | Browser | Version
------------ | ------------ | ------------- | ------------- | ------------- | -------------
1 | Emulator | iPadMini | Tablet | Chrome Emulator | 94.0 |
2 | Emulator | iPhone X | Mobile | Chrome Emulator | 94.0 |
3 | Emulator | iPhone 5/SE | Mobile | Chrome Emulator | 94.0 |

- Below are the test results for testing the website requirements against a range of browsers and devices
- For the purpose of the screenshots I used a Chrome emulator for desktop, tablet and mobile


### Feature 1 Navigation Bar and Homepage
#### User Stories Steps 1
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

### Feature 2 Footer
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
Step 6 | The edit product page is displayed | [Desktop]  | [Tablet]  | [Mobile]  |  |
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
Step 3 | The users order details is displayed | [Desktop]  | [Tablet]  | [Mobile]  | |

### Feature 07 Product Management
#### User Story 07-1
- User Story 10.1: As an admin user I can add a product by clicking on the Product Management link in My Account. I must enter a name, category, price, colour, code, description and can optionally add a feature (1-4), has Sizes(Unknown, Yes, No), Rating, Pre-sale price, Image url, upload an image and click the 
Add Product button. Clicking cancel navigates the user to the product page.

#### User Story Steps 07-1
- Step 1: As an admin user login navigate to Product Management under MyAccount, and add details to a product and click the Add Product button
- Step 2: Click on the product detail for the product

#### User Story Testing Results 07-1
Step| Result | Desktop | Tablet | Mobile | Status
------------ | ------------ | ------------- | ------------- | ------------- | -------------
Step 1 | The add product page is displayed | [Desktop](readme/testing/addproduct_desktop.png)  | [Tablet](readme/testing/addproduct_ipad.png)  | [Mobile](readme/testing/addproduct_iphone.png)  | Passed |
Step 2 | The product detail is displayed | [Desktop](readme/testing/addedproduct_desktop.png)  | [Tablet](readme/testing/addedproduct_ipad.png)  | [Mobile](readme/testing/addedproduct_iphone.png)  | Passed |

#### User Story 07-2
- User Story 10.2: As an admin user I can edit a product by clicking on the Edit button on the Products page for the product. I can update thea name, category, price, colour, code, description, has Sizes(Unknown, Yes, No), Rating, Pre-sale price, Image url, update an image and click the 
Edit Product button. Clicking cancel navigates the user to the product page
#### User Story Steps 07-2
- Step 1: As an admin user login navigate to a product in the products page and click on a product, and click the Edit button
- Step 2: Update the product, for example the price
#### User Story Testing Results 07-2
Step| Result | Desktop | Tablet | Mobile | Status
------------ | ------------ | ------------- | ------------- | ------------- | -------------
Step 1 | The edit product page is displayed | [Desktop](readme/testing/edit_product_desktop.png)  | [Tablet](readme/testing/edit_product_ipad.png)  | [Mobile](readme/testing/edit_product_iphone.png)  | Passed |
Step 2 | The product detail is updated with the news price| [Desktop](readme/testing/edited_product_desktop.png)  | [Tablet](readme/testing/edited_product_ipad.png)  | [Mobile](readme/testing/edited_product_iphone.png)  | Passed |

#### User Story 07-3
- User Story 10.3: As an admin user I can delete a product by clicking on the Delete button on the product. A modal will appearing asking to confirm, and a message displayed once I confirm.
#### User Story Steps 07-3
- Step 1: As an admin user login navigate to a product in the products page and click the Delete button
- Step 2: Delete the product
#### User Story Testing Results 07-3
Step| Result | Desktop | Tablet | Mobile | Status
------------ | ------------ | ------------- | ------------- | ------------- | -------------
Step 2 | The product is deleted and the count is reduced| [Desktop](readme/testing/delete_product_desktop.png)  | [Tablet](readme/testing/delete_product_ipad.png)  | [Mobile](readme/testing/delete_product_iphone.png)  | Passed |


#### User Stories feature 08 shopping bag
- User Story 08.1: As a regular user I can click on a product, set the size(if applicable) and quantity, click Add to Bag and the product will be added to my bag, a message displayed, and a toast will be displayed with the bag contents
- User Story 08.2: As a regular user I can click on the bag icon, I will be brought to my bag. If there are no items in the bag, a message will be displayed
- User Story 08.3: As a regular user I can click on the bag icon, I will be brought to my bag. If there are items, the product image, detail, price, quantity, subtotal will be displayed for the item. The bag total, delivery(if applicable), grand total would be displayed
- User Story 08.4: As a regular user I can update the quantity or remove an item from my shopping bag
- User Story 08.5: As a regular user I can click on the Secure Checkout button on the bag page or toast message, and I will be brought to the Checkout page
- User Story 08.6: As a regular user on the checkout page I can set my details(Full Name, email address, both mandatory) and Delivery Information(Phone Number(mandatory), Street Address 1(mandatory), Street Address 2, Town or City(mandatory, County, State or Locality, Postal Code and Country(mandatory), which is populated from my profile if filled in
- User Story 08.7: As a regular user on the checkout page I can view the order summary(item image, title, size, quantity, subtotal, order total, delivery, grand total)
- User Story 08.8: As a regular user on the checkout page if I click "Save this delivery information to my profile", the details entered will be saved on the users profile
- User Story 08.9: As a regular user on the checkout page I can enter a credit card number(16 digits), expiry date(2 digits/2digits), cvc(3 digits) and a postal code(up to 5 digits), these fields are mandatory
- User Story 08.10: As a regular user on the checkout page if I click the Keep Shopping button I will be navigated to the products page
- User Story 08.11: As a regular user on the checkout page if I click the Complete Order button, and the transaction is not successful, a message will be displayed
- User Story 08.12: As a regular user on the checkout page if I click the Complete Order button, and the transaction is successful, the user will be navigated to a checkout success page, and an email is sent to the user
- User Story 08.13: As a regular user on the checkout page if I click the Complete Order button, and the transaction is successful, the order is saved to my order history in My profile page
- User Story 08.14: As a regular user on the checkout success page, the Order details will be displayed (Order number, Order date/time, Full NameStreet Address 1, Street Address 2, Town or City, County, State or Locality, Postal Code and Country, Phone Number, Order Total, Deliver, Grand Total) and a link to the sales item page is displayed
- User Story 08.15: As a regular user not logged in, I can add items to my bag and make a purchase

#### User Stories Steps 08
Note: Some screenshots show dollars, I have since changed all instances to euros
1. As a regular user add some items to your bag, so the order is less than 99 euros
2. Empty the bag
3. Add the items back into the bag
4. Add the items back into the bag, and Update the quantity on one item by one, so the order goes above 99 euros
5. Checkout the order
6. Complete the order form
7. Go to the order details on the users my profile page
8. Logout, and as a user not logged in add items to a bag 
8. Checkout and complete the purchase
#### User Story Testing Results 08
Step| Result | Desktop | Tablet | Mobile | Status
------------ | ------------ | ------------- | ------------- | ------------- | -------------
Step 1 | The items are added to the bag, and there is a delivery charge(10%) and message displayed | [Desktop](readme/testing/add_product_to_bag_desktop.png)  | [Tablet](readme/testing/add_product_to_bag_ipad.png)  | [Mobile](readme/testing/add_product_to_bag_iphone.png)  | Passed |
Step 2 | A message "Your bag is empty" is displayed with a button to go shopping | [Desktop](readme/testing/empty_bag_desktop.png)  | [Tablet](readme/testing/empty_bag_ipad.png)  | [Mobile](readme/testing/empty_bag_iphone.pngG)  | Passed |
Step 3 | The items are added to the bag, and there is a delivery charge(10%) and message displayed | [Desktop](readme/testing/shopping_bag_desktop.png)  | [Tablet](readme/testing/shopping_bag_ipad.png)  | [Mobile](readme/testing/shopping_bag_iphone.png)  | Passed |
Step 4 | The items are added to the bag, and there is no delivery charge | [Desktop](readme/testing/no_delivery_charge_desktop.png)  | [Tablet](readme/testing/no_delivery_charge_ipad.png)  | [Mobile](readme/testing/no_delivery_charge_iphone.png)  | Passed |
Step 5 | The user receives an email(confirmation) | [Desktop]()  | [Tablet]()  | [Mobile]()  | |
Step 6 | The order is complete | [Desktop](readme/testing/complete_order_form_desktop.png)  | [Tablet](readme/testing/complete_order_form_ipad.png)  | [Mobile](readme/testing/complete_order_form_iphone.png)  | Passed |
Step 7 | The order is displayed on the "my profile" page | [Desktop](readme/testing/order_history_desktop.png)  | [Tablet](readme/testing/order_history_ipad.png)  | [Mobile](readme/testing/order_history_iphone.png)  | Passed |
Step 8 | The purchase is successful and the checkout success page is displayed | [Desktop](readme/testing/thank_you_desktop.png)  | [Tablet](readme/testing/thank_you_ipad.png)  | [Mobile](readme/testing/thank_you_iphone.png)  | Passed |


### Feature 9 Admin
#### User Story 9-1
- User Story 13.1: As an admin user I can view users orders in the django admin page and can view order number, date, full name, order total, delivery cost, grand total
#### User Story Steps 9-1
- Step 1: As an admin user login navigate to https://8000-lime-jackal-9mgfiw2b.ws-eu33.gitpod.io/admin/checkout/order/
#### User Story Testing Results 9-1
Step| Result | Result  | Status
------------ | ------------ | ------------- | ------------- 
Step 1 | The orders are displayed | [Result](/workspace/CI-MS5-PinkAccessories/readme/testing/admin_order_desktop.png)  | Passed |

#### User Story Expected Result 9-2
- User Story 9.2: As an admin user I can view products in the django admin page and can view a products code, name, category, has sizes, price, presale price, rating, image, image url
#### User Story Steps 9-2
- Step 1: As an admin user navigate to https://8000-lime-jackal-9mgfiw2b.ws-eu33.gitpod.io/admin/products/product/
#### User Story Testing Results 9-2
Step| Result | Result  | Status
------------ | ------------ | ------------- | ------------- 
Step 1 | The products are displayed | [Result](readme/testing/admin_products.png)   | Passed |

#### User Story 9-3
- User Story 13.10: As an admin user I can view users in the django admin page and can search by username and email address and  filter by staff status, superuser status and active status
#### User Story Steps 9-10
- Step 1: As an admin user navigate to  and filter on non superuser status
#### User Story Testing Results 9-10
Step| Result | Result  | Status
------------ | ------------ | ------------- | ------------- 
Step 1 | The non superuser users are displayed | [Result](readme/testing/admin_users.png)   | Passed |


#### User Story 9.11
- User Story 13.15: As an admin user I can view categories in the django admin page and can view a category name and friendly name
#### User Story Steps 9.11
- Step 1: As an admin user navigate to https://8000-lime-jackal-9mgfiw2b.ws-eu33.gitpod.io/admin/products/category/
#### User Story Testing Results 9.11
Step| Result | Result  | Status
------------ | ------------ | ------------- | ------------- 
Step 1 | The categories are displayed | [Result](readme/testing/admin_categories.png)   | Passed |

# Code Validators and Website Analysis
The website's pages was tested against the following validators:

## HTML Markup Validation Service
I used https://validator.w3.org/ to validate the html files

Page | Result | Test Detail/Screenshot
------------ | ------------- | -------------
bag/templates/bag/bag.html  | 0 errors and 0 contrast errors| [Results](readme/testing/bag_w3validation.png) 
checkout/templates/checkout/checkout.html | 0 errors and 0 contrast errors| [Results](readme/testing/checkout_w3validation.png)  
checkout/templates/checkout/checkout_success.html | 0 errors and 0 contrast errors| [Results](readme/testing/checkout_success_w3validation.png)  
home/templates/home/index.html | 0 errors and 0 contrast errors| [Results](readme/testing/index_w3validation.png)
products/templates/products/add_product.html | 0 errors and 0 contrast errors| [Results](readme/testing/add_product_w3validation.png)
products/templates/products/edit_product.html | 0 errors and 0 contrast errors| [Results](readme/testing/add_product_w3validation.png)  
products/templates/products/product_detail.html | 0 errors and 0 contrast errors| [Results](readme/testing/products_detail_w3validation.png) 
products/templates/products/products.html | 0 errors and 0 contrast errors| [Results](readme/testing/products_w3validation.png)     
profile/templates/profile/profile.html | 0 errors and 0 contrast errors| [Results](readme/testing/profile_w3validation.png)  
profile/templates/profile/order_history.html | 0 errors and 0 contrast errors| [Results](readme/testing/order_history_w3validation.png)  
templates/allauth/account/login.html | 0 errors and 0 contrast errors| [Results](readme/testing/login_w3validation.png)
templates/allauth/account/logout.html | 0 errors and 0 contrast errors| [Results](readme/testing/logout_w3validation.png)
templates/allauth/account/register.html | 0 errors and 0 contrast errors| [Results](readme/testing/registraion_w3validation.png) 
templates/allauth/account/password_change.html | 0 errors and 0 contrast errors| [Results](readme/testing/forgot_password_w3validation.png)
templates/allauth/account/password_reset.html | 0 errors and 0 contrast errors| [Results](readme/testing/reset_password_w3validation.png)
templates/allauth/account/password_reset_done.html | 0 errors and 0 contrast errors| [Results](readme/testing/password_reset_done_w3validation.png)
templates/allauth/account/verification_sent.html | 0 errors and 0 contrast errors| [Results](readme/testing/password_reset_sent_w3validation.pngg)
<br>

## CSS Validation Service
I used https://jigsaw.w3.org/css-validator/ to validate the css(style.css)
<p>
    <a href="https://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="https://jigsaw.w3.org/css-validator/images/vcss"
            alt="Valid CSS!" />
    </a>
</p>

Page | Result | Test Detail/Screenshot
------------ | ------------- | -------------
static/css/base.css | Passed, No errors found | [Results](readme/testing/base_css_validation.png) 
checkout/static/checkout/css/checkout.css | Passed, No errors found | [Results](readme/testing/checkout_css_validation.png)  
