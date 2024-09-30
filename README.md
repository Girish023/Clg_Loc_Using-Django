# College Course & Loc Using Django

## Overview

DjangoVarity is a Django-based web application designed to manage and review various types of projects related to technology and data science. The application allows users to add projects, submit reviews, and manage subjects linked to these projects.

## Models

### DjangoVarity

This model represents a variety of Django-related projects.

- **Fields:**
  - `name`: The name of the project (CharField).
  - `image`: An image representing the project (ImageField).
  - `date_added`: The date and time when the project was added (DateTimeField).
  - `type`: The type of project, selected from predefined choices (CharField).
  - `description`: A detailed description of the project (TextField).

- **Choices for `type`:**
  - ML (Machine Learning)
  - LR (Learning)
  - AI (Artificial Intelligence)
  - DS (Data Science)
  - SC (Science)

### ProjectReview

This model allows users to review projects.

- **Fields:**
  - `project`: A foreign key linking to the `DjangoVarity` project (ForeignKey).
  - `user`: A foreign key linking to the user who wrote the review (ForeignKey).
  - `rating`: An integer rating for the project (IntegerField).
  - `comments`: Text feedback on the project (TextField).
  - `date_added`: The date and time when the review was submitted (DateTimeField).

### Subjects

This model represents subjects associated with various projects.

- **Fields:**
  - `name`: The name of the subject (CharField).
  - `location`: The location related to the subject (CharField).
  - `sub_variety`: A many-to-many relationship linking to `DjangoVarity` projects (ManyToManyField).

### Certificate

This model stores certification information for a specific project.

- **Fields:**
  - `Certi`: A one-to-one relationship linking to `DjangoVarity` (OneToOneField).
  - `certificate_number`: A unique certificate number (CharField).
  - `issued_data`: The date when the certificate was issued (DateTimeField).
  - `valid_untill`: The expiration date of the certificate (DateTimeField).

## Installation

1. Clone the repository:

   ```bash
   git clone (https://github.com/Girish023/Clg_Loc_Using-Django.git
   cd DjangoVarity
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:

   ```bash
   python manage.py migrate
   ```

5. Create a superuser to access the admin interface:

   ```bash
   python manage.py createsuperuser
   ```

6. Run the server:

   ```bash
   python manage.py runserver
   ```

## Usage

- Access the application at `http://127.0.0.1:8000/`.
- Use the Django admin panel to manage projects, reviews, and subjects.

## Contributing

Feel free to submit issues or create pull requests to contribute to the project. 

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

- Django framework
- All contributors to the project
