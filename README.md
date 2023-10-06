# Flask Blogging Platform README

# Project overview

Welcome to the Flask Blogging Platform! This is a simple and customizable web application built with Python and Flask, designed to help you create and manage your own blogs. Whether you're a blogger looking for a new platform or a developer interested in building on top of this project, this guide will help you get started.

## Features and functionalities

- **User Registration and Authentication:** Users can create accounts, log in securely, and manage their profiles.
- **Create and Edit Posts:** Users can easily create, edit, and delete blog posts with a user-friendly interface.
- **Categories and Tags:** Organize your content by categorizing posts and adding tags for easy navigation.
- **Commenting:** Engage with your readers through comments on your blog posts.
- **Rich Text Editor:** A WYSIWYG editor allows for easy formatting and styling of your content.
- **Responsive Design:** The platform is designed to work seamlessly on both desktop and mobile devices.
- **Search Functionality:** Users can search for specific posts or topics.
- **SEO-Friendly:** Customize metadata and optimize your blog posts for search engines.
- **User Dashboard:** Registered users have access to a dashboard where they can manage their posts, profile, and settings.
- **Social Media Sharing:** Share your blog posts effortlessly on various social media platforms.
- **Analytics:** Gain insights into your blog's performance with basic analytics.
- **Admin Panel:** Administrators can manage users, posts, and comments.

# Technologies used

This project uses the following programming technologies:
                                 1. **HTML**
                                 2. **CSS**
                                 3. **PYTHON**
                                 4. **FLASK**
                                 5. **JAVASCRIPT**

## Getting Started

To set up and run the Flask Blogging Platform, follow these steps:

1. **Clone the Repository:** Clone this repository to your local machine.

   ```bash
   git clone <repository_url>
   cd flask-blogging-platform
   ```

2. **Install Dependencies:** Install the required Python packages.

   ```bash
   pip install -r requirements.txt
   ```

3. **Database Setup:** Configure your database connection in the `config.py` file. By default, SQLite is used, but you can use other databases like PostgreSQL or MySQL.

4. **Environment Variables:** Create a `.env` file with the following variables:

   ```env
   FLASK_APP=app.py
   FLASK_ENV=development  # Change to 'production' for production deployment
   SECRET_KEY=<your_secret_key>
   DATABASE_URI=<your_database_uri>
   ```

5. **Database Migration:** Apply the database migrations to create the necessary tables.

   ```bash
   flask db upgrade
   ```

6. **Start the Application:** Run the Flask app.

   ```bash
   flask run
   ```

7. **Access the Application:** Open a web browser and navigate to `http://localhost:5000` to access the Flask Blogging Platform.

## Project link and demo(Project's prototype)

The following is the link to the final demo of the project at figma: https://www.figma.com/file/dUdS3WvE6nu4XLyeTMtb1y/Chatter-project-(Copy)?type=design&node-id=7-8&mode=design&t=hT8o9LBEUsskV9Jc-0

## Link to project's flow chart
Below is a link to show the flow chart of the project.

https://lucid.app/lucidchart/009cd9a6-2266-4434-a198-7da1efc88216/edit?viewport_loc=-458%2C1000%2C2688%2C1290%2C0_0&invitationId=inv_97a78e29-d4ba-44e7-88ef-20861dbedfb1

## Customization

The Flask Blogging Platform is highly customizable. You can modify the templates, styles, and functionality to suit your specific needs.

- Templates are located in the `templates` directory.
- Static assets (CSS, JavaScript, images) are in the `static` directory.
- Additional features and routes can be added to the `app.py` file.

## Contributing

This project is free and open source. Any contributions are further welcome for the overall improvement of the project.If any issues feel free to contact me through the email: charleswilliam26@gmail.com.