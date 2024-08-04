# Book Exchange Club API

## Overview

The **Book Exchange Club API** provides a robust backend service for the Book Exchange Club web application, facilitating book exchanges between users without monetary transactions. This API enables seamless integration with the web application by delivering essential book information and supporting various functionalities required for the platform.

## Features

- **Custom API**: Built with Python Flask, this API delivers comprehensive book information, including title, author, description, cover image, and other relevant details, formatted in JSON.
- **Endpoints**: Provides various endpoints to manage book listings, user profiles, and exchange requests.
- **Data Management**: Retrieves and stores book data efficiently, ensuring accurate and up-to-date information for the web application.
- **User Interaction**: Supports functionalities such as searching for books, listing available titles, and managing exchange requests.

## Purpose

The Book Exchange Club API aims to:

- Facilitate the exchange of books by providing a centralized service for managing book data and user interactions.
- Enhance the Book Exchange Club web application by providing reliable and structured data.
- Promote a community-driven approach to book swapping while supporting sustainable practices.

## API Endpoints

- **Endpoint**: `/`
- **Method**: `GET`
- **Description**: Returns a welcome message and a list of available links in the API.
- **Response**:
  ```html
  <h1>This is a books API</h1>
  <h2>available links</h2>
  <h2>/popularCategories</h2>
  <link rel="shortcut icon" href="{{ url_for('static', filename='favicon.ico') }}">
