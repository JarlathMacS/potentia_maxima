# Potentia | Maxima

## Features

This web application has the following pages:

- landing home page
- sign up page
- log in page
- log out page
- client home page
- coaching post detail page
- about page
- free consultation request page
- 404 error page
- 500 error page

### Access to pages according to the user status:

| Page Name                      | Site visitor | Client user |
| ------------------------------ | ------------ | ----------- |
| landing home page              | Y            | Y           |
| sign up page                   | Y            | Y           |
| log in page                    | Y            | Y           |
| log out page                   | N            | Y           |
| client home page               | N            | Y           |
| coaching post detail page      | N            | Y           |
| about page                     | Y            | Y           |
| free consultation request page | Y            | Y           |
| 404 error page                 | Y            | Y           |
| 500 error page                 | N            | Y           |

### Each page has a navbar and a footer:

### Navbar

![Navbar](documentation/features/navbar/navbar.png)

Navbar has the following links:

- Home
- About, which leads to the about page
- Enquire, which leads to the free consultation request page and form

If user is not signed in:

- Sign Up, which leads to the sign up page
- Log In, which leads to the log in page

If user is signed in:

- Log Out, which leads to the log out confirmation page

The remaining navbar links are:

- at the far left is a logo of the coaching web site:

![Logo](documentation/features/navbar/navbar_logo.png)

- at the far right is the coaching branding:

![Brand](documentation/features/navbar/brand.png)

When the user hovers their cursor over each menu item, the colour changes from
blue to orange, except in the case of the logo, from orange to blue:

![Navbar Colour](documentation/features/navbar/navbar_menu_colour.png)

The current page is indicated in the navbar menu items by its colour changing
to orange:

![Navbar Page](documentation/features/navbar/navbar_menu_colour_zoom.png)

On mobile screens, the navbar looks like this:

![Navbar Mobile](documentation/features/navbar/navbar_mobile.png)

which when the icon:

![Navbar Mobile Icon](documentation/features/navbar/navbar_hamburger.png)

is clicked, expands to reveal:

![Navbar Mobile Expanded](documentation/features/navbar/navbar_mobile_expand.png)

### Footer

![Footer](documentation/features/footer/footer.png)

The footer has the following sections:

- Logo on the left side, with link to Instagram page of the Coach:

![Logo and Insta](documentation/features/footer/footer_logo.png)

- Copyright on the right side, with links to GitHub and LinkedIn pages of the
  website creator:

![Website Creator](documentation/features/footer/footer_credit.png)

### Landing Home Page

![Landing Home Page](documentation/features/landing_home_page/landing_home_page.png)

On the left of the desktop page is a collage of inspiring hero images of the
coach at exercise, which is the very first engagement a visitor has with the
site:

![Landing Images](documentation/features/landing_home_page/landing_hero_image_collage.png)

The Landing home page is arrived at by anyone who is not already signed in to
the application. Here, the visitor is posed a single question:

![Landing Dialogue](documentation/features/landing_home_page/landing_dialogue.png)

together with an orange action button of "Sign Up":

![Landing Button](documentation/features/landing_home_page/landing_dialogue_zoom.png)

which will take them to the Sign Up page, where they can sign up to become a
client.

### Sign Up Page

![Sign Up Page](documentation/features/sign_up_page/sign_up.png)

This page has a sign up form, which has a title and input fields for the user 
to fill in.

In the header of the form, there is a title of "Sign Up":

![Sign Up Page Header](documentation/features/sign_up_page/signup_page_header.png)

Underneath, there is a subtitle of "Already a Client?" and a link "Log In", 
which leads to the log in page:

![Sign Up Page Log In](documentation/features/sign_up_page/signup_page_login.png)

Under the form's header, there are the following fields:

![Sign Up Page Fields](documentation/features/sign_up_page/signup_page_fields.png)

The user is required to fill out these fields:
- Username (to let the user be addressed by their username)
- Password (to let the user log in)
- Password (again) (to let the user log in)

If the user inputs an invalid email address format, the email field will be 
highlighted:

![Sign Up Page Email Field](documentation/features/sign_up_page/signup_page_error_email.png)

If the user leaves a field empty, that field will be highlighted:

![Sign Up Page Empty Field](documentation/features/sign_up_page/signup_page_error_empty_field.png)

The form lists 4 different password instructions:

![Sign Up Page Password Instructions](documentation/features/sign_up_page/signup_page_password_instructions.png)

If the user inputs an invalid password, or the passwords don't match, or the
instructions are not adhered to, the password fields will be highlighted:

![Sign Up Page Password Field](documentation/features/sign_up_page/signup_page_error_password_1.png)
![Sign Up Page Password Field](documentation/features/sign_up_page/signup_page_error_password_2.png)
![Sign Up Page Password Field](documentation/features/sign_up_page/signup_page_error_password_3.png)

If the user inputs a duplicate username, the username field will be highlighted:

![Sign Up Page Username Field](documentation/features/sign_up_page/signup_page_error_username.png)


### Log In Page

![Log In Page](documentation/features/log_in_page/login_page.png)

This page has a log in form, which has a title and input fields for the user 
to fill in.

In the header of the form, there is a title of "Log In":

![Log In Page Header](documentation/features/log_in_page/login_page_header.png)

Underneath, there is a subtitle of "Welcome back to POTENTIA MAXIMA! Please log 
in. Not yet a Client?" and a link of "Sign Up", which leads to the sign up page:

![Log In Page Sign Up](documentation/features/log_in_page/login_page_signup.png)

Under the form's header, there are the following fields which have to be filled 
out in order to log in:

- Username
- Password

![Log In Page Fields](documentation/features/log_in_page/login_page_fields.png)

If the user makes a mistake in the username or password, the field will be 
highlighted:

![Log In Page Error Field](documentation/features/log_in_page/login_page_error_1.png)

![Log In Page Error Field](documentation/features/log_in_page/login_page_error_2.png)


Under the fields, there is a button "Log In" which leads to the 
[Client Home Page](#client-home-page):

![Log In Page Log In Button](documentation/features/log_in_page/login_page_button.png)

The log in status is shown at the top right of the page, under the brand:

![Log In Page Status](documentation/features/log_in_page/login_status_2.png)


### Log Out Page

![Log Out Page](documentation/features/log_out_page/logout_page.png)

This page has a log out form with a header and a button "Log Out" leading to 
the [Landing Home Page](#landing-home-page):

![Log Out Page Header](documentation/features/log_out_page/logout_page_header.png)

Underneath is the subtitle "Are you sure you want to log out?"

Below this, there is a button "Log Out":

![Log Out Page Button](documentation/features/log_out_page/logout_page_button.png)

The log out status is shown at the top right of the page, under the brand:

![Log Out Page Status](documentation/features/log_in_page/login_status_1.png)


### Client Home Page

[Back to top](#potentia--maxima)

---
