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
Step 2 | The user receives an email where they can reset their password | [Desktop](readme/testing/password_reset_email.PNG)  | [Tablet](readme/testing/password_reset_email.PNG)  | [Mobile](readme/testing/password_reset_email.PNG)  | Passed |
Step 3 | The user can successfully log in | [Desktop](readme/testing/password_updated_desktop.PNG)  | [Tablet](readme/testing/password_updated_tablet.PNG)  | [Mobile](readme/testing/password_updated_mobile.PNG)  | Passed |

