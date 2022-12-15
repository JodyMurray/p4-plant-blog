# Jody's Plant Blog

This is a blog for plant lovers, the site includes blog-like posts, sign-up and edit profile section, featured posts and a newsletter sign-up. Also included is a feature for admin to easily edit and delete blog posts from each blog post page.

This project is the fourth of five projects that needs to be completed in order to receve a diploma in Software Development from The Code Institute.

A live version of this website will be found here: https://jodys-plants.herokuapp.com/


## Table of Contents ##
<details><summary>UX</summary>

- [User Demographic](#user-demographic "User Demographic")
- [Site Goals](#site-goals "Site Goals")
- [User Goals](#user-goals "User Goals")
- [Audience](#audience "Audience")


</details>
<details><summary>User Stories</summary>

- [Site User Stories](#site-user-stories "Site User Stories")
- [Admin Stories](#admin-stories "Admin Stories")

</details>

<details><summary>Design</summary>

- [Colour Scheme](#colour-scheme "Colour Scheme")
- [Typography](#typography "Typography")
- [Wireframes](#wireframes "Wireframes")
- [Images](#images "Images")

</details>
<details><summary>Features</summary>

- [NavBar](#nav_bar "NavBar")
- [Home Landing Page](#home_landing_page "Home Landing Page")
- [Featured Posts](#featured-posts "Featured Posts")
- [Profile Page](#profile-page "Profile Page")
- [Sign-in](#sign-in "Sign-in")
- [Register](#register "Register")
- [Newsletter](#newsletter "Newsletter")
- [CRUD](#crud "CRUD")


</details>

<details><summary>Technologies Used</summary>

- [Languages Used](#languages_used "Languages Used")
- [Python Libraries and API](#python_libraries_and_api "Python Libraries and API")
- [Storing Data](#storing_data "Storing Data")

</details>
<details><summary>Testing</summary>

- [Validator testing](#validator-testing "Validator Testing")
- [Testing and bugs](#testing-and-bugs "Testing and bugs")
- [Fixed Bugs](#fixed-bugs "Fixed Bugs") 
- [Unfixed Bugs](#unfixed-bugs "Unfixed Bugs")
- [Future plans to implement](#future-plans-to-implement "Future plans to implement")

</details>

<details><summary>Deployment</summary>

- [Deployment](#deployment "Deployment")

</details>

<details><summary>Acknowledgements</summary>

- [Acknowledgements](#acknowledgements "Acknowledgements")

</details>

<details><summary>Sources</summary>

- [Sources](#sources "Sources")

</details>

------------------------------------------------------------------------------------------------------------

## UX 

### User Demographic

This application has been designed for users of all ages who love to garden and learn new things about plants.
It also includes a feature to create and personalise a profile with a profile picture and a biography entry, and with this you can comment on blog posts, to give more advice or ask questions!

### Site Goals

To build a platform to allow users to read blog posts, make a profile and comment on posts and allow them to also sign up for a newsletter sent to their email. Also included is admin access through the website for the admin to add, update or delete posts from each blog post page. Which allows the admin to easily see how a post would look with just the click of a button.


### User Goals
To engage with topics that interest them, make a personalised profile to feel welcome to the site and encourages them to explore the site and all it has to offer.

### Audience
For anyone who has an interest in plants and gardening of all sorts! Users of all ages and all levels of skills in gardening.

## User Stories

### Site User Stories

### Admin Stories

## Design

### Colour Scheme

The colour scheme chosen works with the theme of the topic chosen for the website. 
- The colour chosen for headings is #2F6844.
- The background colour is an easy on the eyes light green #FFFAF0.
- And the hovered over buttons turn a light shade of grey thanks to bootstrap secondary theme.

<br>

![screenshot](media/colourscheme.png)



### Typography

All fonts are from the Google Fonts library.The following fonts were chosen for the page:

- 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif for the navbar.
- Satisfy for each page heading and the heading for the user's profile page.
- Verdana, Geneva, Tahoma, sans-serif for the body font and content.
- Pacifico font for the headings in the "health" section on the home page.


### Wireframes

![screenshot](media/wireframes1.png)

<br>

![screenshot](media/wireframes2.png)
 <br>

![screenshot](media/wireframes3.png)


### Images

- All images were found through google and stored using Cloudinary.

## Features

### NavBar

- The Navbar is sticky, so it can show login options constantly and home page redirection.

![screenshot](media/navbar.png)

- For responsive design, the Navbar collapses into a dropdown menu for screens 768px and below.

![screenshot](media/navbar2.png)


### Home Landing Page

- The landing/home page brings you to the blog posts.
- Each card brings you to the blog post page, featuring tips, images and a comment and like section.

![screenshot](media/landing-page.png)
![screenshot](media/blog-area.png)

- Scrolling down the index page we have a "Quick Tips Section":

![screenshot](media/quick-tips.png)

- A common mistakes section:

![screenshot](media/common-mistakes.png)

- A section on why plants are good for your health:

![screenshot](media/health.png)

- And finally for the landing page, the Footer:

![screenshot](media/footer.png)

### Featured Posts 

- Featured posts is an option in the Navbar and brings you to a HTML with two cards, which would ideally be changed seasonly.

![screenshot](media/featured.png)

- The first Featured Post is called "Winter is Coming":

![screenshot](media/winter.png)

- The other card features a post all regarding pets and their safety, along with how to keep the plants safe too!

![screenshot](media/pets.png)

### Profile Page

- Once you sign up to a profile, you'll get redirected to your very own Profile page which you can edit by adding your name, profile picture and a bio!
- Also featured is a message that pops up indicating a successful login!

![screenshot](media/profile.png)

- Here is the edit profile page:
- Updating your profile will show a success message on the index page.

![screenshot](media/edit-profile.png)

### Sign-in

- The Sign up page requires username and password to sign in, including a "forgot password" section.

![screenshot](media/signin.png)

### Register

- The register page requires specific information to sign up for a profile, and includes a social media sign in section.

![screenshot](media/signup.png)

### Newsletter

- The newsletter feature does not show up until you sign into your account, then you can spot it in the Navbar.

- The Newsletter feature allows you to signup for the site's ongoing newsletter with featured posts about plants.
- You can submit your email, after clicking the "Newsletter" button on the Navbar, and from the newsleter page you can choose to be redirected to an unsubscribe page to unsubscribe your email from the newsletter.
- I came across some issues implementing this feature. Attempts to use GMAIL failed as they took away this feature just this year, I will include an option to check the results of this feature with a free email service called mailtrap.io. 
- From mailtrap.io it is possible to see the template newsletter is being sent and linking the email used by the user.

![screenshot](media/newsletter.png)
<br>
![screenshot](media/unsub.png)


- Once you unsubscribe, you will see a message confirming that your email has been removed from the database.

![screenshot](media/unsubscribe.png)

### CRUD 














