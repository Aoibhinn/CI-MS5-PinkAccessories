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
Step 2 | The homepage is displayed with a header logo(desktop), search box(expands on tablet/mobile), My account, Favourites and shopping bag icons. My Profile/Logout is visible under My Account and the footer contains links for My Profile, News and Sale   | [Desktop] | [Tablet]  | [Mobile] |  |
Step 3 | Products on the page are filtered by Price (Low-High) | [Desktop] | [Tablet]  | [Mobile]  |  |
Step 4 | Products on the page are filtered by Rating (High-Low) | [Desktop]  | [Tablet] | [Mobile] |  |
Step 5 | Products on the page are filtered by Category (A-Z) | [Desktop]  | [Tablet]  | [Mobile] |  |
Step 6 | Products on the page are filtered by Necklaces | [Desktop] | [Tablet]  | [Mobile] |  |
Step 7 | Products on the page are filtered by Earrings | [Desktop]  | [Tablet]  | [Mobile]  |  |
Step 8 | Products on the page are filtered by Bracelets | [Desktop]| [Tablet]  | [Mobile]  | |
Step 9 | Products on the page are filtered by Scarves | [Desktop]| [Tablet]  | [Mobile]  | |
Step 10 | Products on the page are filtered by Hats | [Desktop]| [Tablet]  | [Mobile]  | |
Step 11 | Products on the page are filtered by Facinators | [Desktop]| [Tablet]  | [Mobile]  | |
Step 12 | Products on the page are filtered by Totes | [Desktop]| [Tablet]  | [Mobile]  | |
Step 13 | Products on the page are filtered by Clutchs | [Desktop]| [Tablet]  | [Mobile]  | |
Step 14 | The user is logged out | [Desktop]  | [Tablet]  | [Mobile] | |
Step 15 | The homepage is displayed with a header logo(desktop), search box(expands on tablet/mobile), My Account and shopping bag icons. Product Management/News Item Management/My Profile/Logout is visible under My Account and the footer contains links for Product Management  | [Desktop]  | [Tablet]  | [Mobile]  |  |


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
Step 1 | The user registers for an account | [Desktop]  | [Tablet]  | [Mobile]  |  |
Step 2 | The user receives the email | [Desktop]  | [Tablet]  | [Mobile]  |  |
Step 3 | The user clicks on the verification link | [Desktop] | [Tablet] | [Mobile]  |  |
Step 4 | The user confirms the email address | [Desktop]  | [Tablet]  | [Mobile] |  |
Step 5 | The user logs in to the site | [Desktop]  | [Tablet]  | [Mobile] |  |
Step 6 | A message is displayed to the user | [Desktop]  | [Tablet] | [Mobile]  |  | 

