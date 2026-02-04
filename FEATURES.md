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

The form lists four different password instructions:

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

This page is accessible only by those authenticated users of the application.

![Client Home Page](documentation/features/client_home_page/client_home_page.png)

The Client Home Page displays multiple cards at a time, with each card 
containing a different coaching post:

![Client Home Page Card](documentation/features/client_home_page/client_home_page_card.png)

in a grid format on the desktop.  Each card contains an image:

![Client Home Page Card Image](documentation/features/client_home_page/client_home_page_card_image.png)

a title:

![Client Home Page Card Title](documentation/features/client_home_page/client_home_page_card_title.png)

and an excerpt:

![Client Home Page Card Excerpt](documentation/features/client_home_page/client_home_page_card_excerpt.png)

Also shown are the coach's name who authored the coaching post:

![Client Home Page Card Author](documentation/features/client_home_page/client_home_page_card_author.png)

and the date it was created:

![Client Home Page Card Created On](documentation/features/client_home_page/client_home_page_card_created_on.png)

On the desktop there will be six coaching posts to a page, arranged in two rows
of three posts each.  On the mobile version, the coaching posts are displayed 
vertically in one row:

![Client Home Page Mobile](documentation/features/client_home_page/client_home_page_mobile.png)

At the bottom of the page are the navigation buttons, either "PREV" or "NEXT" or
both:

![Client Home Page Button](documentation/features/client_home_page/button_next.png)
![Client Home Page Button](documentation/features/client_home_page/button_prev.png)
![Client Home Page Button](documentation/features/client_home_page/button_prev_next.png)


### Coaching Post Detail Page

This page is accessible only by those authenticated users of the application.

![Coaching Post Detail Page](documentation/features/coaching_post_detail_page/detail_page_a.png)
![Coaching Post Detail Page](documentation/features/coaching_post_detail_page/detail_page_b.png)

The Coaching Post Detail Page displays a single coaching post in its entirety.
It also displays all progress comments made on the coaching post, either by the 
client users, or by the coach/es.

At the top of the post is a masthead:

![Coaching Post Detail Mast](documentation/features/coaching_post_detail_page/detail_mast.png)

containing the coaching post title:

![Coaching Post Detail Mast Title](documentation/features/coaching_post_detail_page/detail_mast_title.png)

the authorship and creation details:

![Coaching Post Detail Mast Author](documentation/features/coaching_post_detail_page/detail_mast_author.png)

and to the right is the same image as was displayed on the Client Home Page in
the card:

![Coaching Post Detail Mast Image](documentation/features/coaching_post_detail_page/detail_mast_image.png)

What follows is the text of the coaching post, along with any images, videos,
links, etc. that the coach wants to use:

![Coaching Post Detail Post](documentation/features/coaching_post_detail_page/detail_post.png)

Next is the progress comments section:

![Coaching Post Detail Comments](documentation/features/coaching_post_detail_page/detail_comments.png)

At the beginning of this section, the number of progress comments currently 
under this coaching post is displayed:

![Coaching Post Detail Comments Count](documentation/features/coaching_post_detail_page/detail_comments_count.png)

Next is a title of "Progress Comments":

![Coaching Post Detail Comments Title](documentation/features/coaching_post_detail_page/detail_comments_title.png)

Then each comment is displayed, starting with the oldest one at the top, and the
most recent one at the bottom:

![Coaching Post Detail Comments](documentation/features/coaching_post_detail_page/detail_comments_a.png)

At the top of each comment is listed the author's username, and the date and 
time it was created:

![Coaching Post Detail Comments Header](documentation/features/coaching_post_detail_page/detail_comments_a_header.png)

If the user that is logged in is the author of any comments, these will display
with two buttons beneath the comment, "Delete" and "Edit":

![Coaching Post Detail Comments Crud](documentation/features/coaching_post_detail_page/detail_comments_crud.png)

When the blue "Edit" button:

![Coaching Post Detail Comment](documentation/features/coaching_post_detail_page/detail_comment.png)

is clicked, the focus is shifted to the form entitled "Leave a progress 
comment" and the body of this form is populated with the content of the user's
existing comment:

![Coaching Post Detail Comments Update](documentation/features/coaching_post_detail_page/detail_comments_update.png)

When the user has made changes and clicks the "Update" button, if there are no
errors, the user is displayed a green confirmation message at the top of the 
page:

![Coaching Post Detail Comments Update Message](documentation/features/coaching_post_detail_page/detail_comments_update_message.png)

When the red "Delete" button is clicked, a modal dialog box appears:

![Coaching Post Detail Comments Delete Modal](documentation/features/coaching_post_detail_page/detail_comments_delete_modal.png)

asking for confirmation of the user's desire to delete the progress comment:

![Coaching Post Detail Comments Delete](documentation/features/coaching_post_detail_page/detail_comments_delete.png)

When the user confirms and clicks the "Delete" button, if there are no
errors, the user is displayed a green confirmation message at the top of the 
page:

![Coaching Post Detail Comments Delete Message](documentation/features/coaching_post_detail_page/detail_comments_delete_message.png)

The user can also create a new progress comment using the form entitled "Leave
a progress comment":

![Coaching Post Detail Comments Create](documentation/features/coaching_post_detail_page/detail_comments_create_form.png)

When the user has written their progress comment and clicks the "Submit" button, if there are no
errors, the user is displayed a green confirmation message at the top of the 
page:

![Coaching Post Detail Comments Create Messages](documentation/features/coaching_post_detail_page/detail_comments_create_message.png)

On mobile screens, the masthead image is not displayed:

![Coaching Post Detail Mobile Mast](documentation/features/coaching_post_detail_page/detail_mobile_a.png)

and the progress comment form is displayed at the bottom of the page instead of
on the right hand side:

![Coaching Post Detail Mobile Form](documentation/features/coaching_post_detail_page/detail_mobile_b.png)


[Back to top](#potentia--maxima)

---
