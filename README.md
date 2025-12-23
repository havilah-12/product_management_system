# Simple Product Management System

A Django-based web application for managing products with user authentication, CRUD operations, category management, search, and filtering capabilities.

## Project Overview

This is a full-stack web application built with Django that allows authenticated users to manage their product inventory. The system provides a clean, responsive interface for adding, viewing, updating, and deleting products with support for categories, images, and advanced filtering.

## Features Implemented

### 1. Authentication System

- ✅ User registration with Django's built-in authentication
- ✅ User login and logout functionality
- ✅ Session-based authentication
- ✅ Protected routes - only logged-in users can manage products
- ✅ Automatic redirect to login page for unauthenticated users

### 2. Product Management (CRUD Operations)

- ✅ **Create**: Add new products with name, description, price, category, and optional image
- ✅ **Read**: View product list with pagination (10 products per page)
- ✅ **Update**: Edit existing products (users can only edit their own products)
- ✅ **Delete**: Remove products with confirmation dialog (users can only delete their own products)

### 3. Product Features

Each product includes:

- Name (required)
- Description (required)
- Price (required, decimal format)
- Category (required, foreign key relationship)
- Image (optional, supports JPG, PNG, GIF)
- Created date (automatically set, displayed in IST)
- Created by (tracks which user created the product)

### 4. Category Management

- ✅ Categories stored in database
- ✅ Each product must belong to a category
- ✅ Category-wise product listing and filtering
- ✅ Products ordered by category name, then by creation date

### 5. Search & Filter

- ✅ Search products by name (case-insensitive)
- ✅ Filter products by category
- ✅ Combined search and filter functionality
- ✅ Visual indicator when category filter is applied (button color changes)

### 6. Frontend Features

- ✅ Django templates with Bootstrap 5.3.2
- ✅ Responsive design for mobile and desktop
- ✅ Modern UI with dark blue theme and cyan accents
- ✅ Form validation with error messages
- ✅ Success/error message alerts (auto-dismiss after 4 seconds)
- ✅ Image display with full view (no cropping)
- ✅ Scrollable product table (max 70vh height)
- ✅ Sticky table header while scrolling
- ✅ Pagination controls with page numbers

### 7. Database

- ✅ SQLite database (default Django database)
- ✅ Proper Django models with relationships
- ✅ Foreign key relationships (Product → Category, Product → User)
- ✅ Database migrations included
- ✅ Timezone set to Asia/Kolkata (IST)

## Technology Stack

- **Backend**: Django 6.0
- **Database**: SQLite
- **Frontend**: HTML5, CSS3, Bootstrap 5.3.2
- **Icons**: Bootstrap Icons
- **Image Processing**: Pillow (PIL)
- **Python**: 3.x

## Setup Instructions

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation Steps

1. **Clone or navigate to the project directory**

   ```bash
   cd "d:\simple product management system\product_mgmt"
   ```
2. **Create and activate a virtual environment (if not already created)**

   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies**

   ```bash
   pip install django pillow
   ```

   Note: Dependencies are already installed in the `venv` folder if using the existing virtual environment.
4. **Run database migrations**

   ```bash
   python manage.py migrate
   ```
5. **Create a superuser (optional, for Django admin)**

   ```bash
   python manage.py createsuperuser
   ```
6. **Run the development server**

   ```bash
   python manage.py runserver
   ```
7. **Access the application**

   - Open your browser and navigate to: `http://127.0.0.1:8000/`
   - Register a new account or login with existing credentials

## Admin Credentials

**Username**: `user123`  
**Password**: `User@123`

> **Note**: This is a test/admin account. For production, change the password immediately or create new superuser accounts.

## Project Structure

```
product_mgmt/
├── manage.py                   # Django management script
├── db.sqlite3                  # SQLite database (created after migrate)
├── README.md                   # Documentation
├── media/                      # User-uploaded media
│   └── products/               # Product images
├── product_mgmt/               # Project settings
│   ├── __init__.py
│   ├── settings.py             # Django settings
│   ├── urls.py                 # Main URL configuration
│   ├── wsgi.py
│   └── asgi.py
├── products/                   # App code
│   ├── __init__.py
│   ├── admin.py                # Admin config
│   ├── apps.py
│   ├── forms.py                # Forms
│   ├── models.py               # Category & Product models
│   ├── tests.py
│   ├── urls.py                 # App routes
│   ├── views.py                # Views
│   └── migrations/             # Database migrations
│       └── 0001_initial.py
├── templates/                  # HTML templates
│   ├── base.html               # Base layout
│   ├── auth/                   # Auth pages
│   │   ├── login.html
│   │   └── register.html
│   └── products/               # Product pages
│       ├── product_list.html
│       ├── product_form.html
│       └── product_confirm_delete.html
└── venv/                       # (Optional) local virtual environment
```

## URL Routes

- `/` - Product list (requires login)
- `/register/` - User registration
- `/login/` - User login
- `/logout/` - User logout
- `/add/` - Add new product (requires login)
- `/edit/<id>/` - Edit product (requires login, only own products)
- `/delete/<id>/` - Delete product (requires login, only own products)
- `/admin/` - Django admin panel (requires superuser)

## Key Features Details

### Pagination

- 10 products per page
- Scrollable table container (max height: 70vh)
- Shows "Showing X of Y products"
- Previous/Next navigation buttons
- Page number links

### Image Handling

- Images stored in `media/products/` directory
- Full image display (no cropping) with `object-fit: contain`
- Images displayed inline on the product list (no modal/new-tab)
- Supports JPG, PNG, GIF formats
- Optional field - products can be created without images

### Time Display

- All timestamps displayed in Indian Standard Time (IST)
- Format: "HH:MM AM/PM IST" and "Month DD, YYYY"
- Timezone configured as `Asia/Kolkata`

### Security Features

- CSRF protection enabled
- User can only edit/delete their own products
- Login required for all product management operations
- Password hashing using Django's default authentication

## Assumptions & Limitations

### Assumptions

1. Users can only manage their own products (created_by field)
2. Categories are managed through Django admin or need to be created manually
3. Images are stored locally in the media directory
4. SQLite is sufficient for development (can be upgraded to PostgreSQL for production)
5. Single user session per account (no concurrent session management)

### Limitations

1. **No Category CRUD in UI**: Categories must be created through Django admin or database directly
2. **No Image Resizing**: Original image sizes are stored (consider adding image optimization for production)
3. **No Bulk Operations**: Products must be edited/deleted individually
4. **No Export Functionality**: No CSV/Excel export for product data
5. **No Advanced Search**: Only basic name search (no description search, price range, etc.)
6. **No Image Validation**: No file size or dimension validation (should be added for production)
7. **Development Settings**: DEBUG=True and insecure SECRET_KEY (must be changed for production)
