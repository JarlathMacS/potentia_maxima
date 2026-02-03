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

| Page Name     | Site visitor  | Client user   |
| ------------- | ------------- | ------------- |
| landing home page                 | Y | Y |
| sign up page                      | Y | Y |
| log in page                       | Y | Y |
| log out page                      | N | Y |
| client home page                  | N | Y |
| coaching post detail page         | N | Y |
| about page                        | Y | Y |
| free consultation request page    | Y | Y |
| 404 error page                    | Y | Y |
| 500 error page                    | N | Y |



### Each page has a navbar and a footer

**Navbar**

![Navbar](documentation/features/navbar/navbar.png)

Navbar has the following links:
- home
- about, which leads to the about page
- enquire, which leads to the free consultation request page and form

If user is not signed in:
- sign up, which leads to the sign up page
- log in, which leads to the log in page

If user is signed in:
- log out, which leads to the log out confirmation page

The remaining navbar links are:
- at the far left is a logo of the coaching web site

![Logo](documentation/features/navbar/navbar_logo.png)
- at the far right is the coaching branding 

![Brand](documentation/features/navbar/brand.png)

When the user hovers their cursor over each menu item, the colour changes from 
blue to orange, except in the case of the logo, from orange to blue.
![Navbar Colour](documentation/features/navbar/navbar_menu_colour.png)

The current page is indicated in the navbar menu items by its colour changing
to orange

![Navbar Page](documentation/features/navbar/navbar_menu_colour_zoom.png)

On mobile screens, the navbar looks like this:

![Navbar Mobile](documentation/features/navbar/navbar_mobile.png)

which when the 

![Navbar Mobile Icon](
    documentation/features/navbar/navbar_hamburger.png
    ) 

is clicked, expands to reveal:

![Navbar Mobile Expanded](
    documentation/features/navbar/navbar_mobile_expand.png
    )
