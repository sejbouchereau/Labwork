## Introduction to the Modification of the Book Management System

Our proposed modification to the book management system simplifies the addition process by introducing a key condition. Now, when entering an ISBN code, instead of immediately generating an error, the system **prompts the user to provide an associated title**. This strategic modification allows the system to switch to title-based searches rather than relying solely on the ISBN, thus avoiding obstacles caused by the absence of the latter, particularly for older books. We believe this solution offers a more flexible and intuitive approach while preserving the integrity of our database. Before implementing this change, we seek your feedback to ensure its effectiveness and acceptance by the team.

### Sequence Diagram: Current

```mermaid
sequenceDiagram
actor Librarian
    Librarian->>+Frontend: Enter code
    Frontend->>+Backend: Verify code

    alt
        Backend-->>Frontend: Valid code
        Frontend->>Backend: Verify if exists
        Backend->>+MongoDB: Verify similarities

        alt
        MongoDB-->>Backend: No similarities
        Backend-->>Frontend: Book doesn't exist
        Frontend->>Librarian: Request book info

        else
        MongoDB-->>-Backend: Similarities
        Backend-->>Frontend: Book exists
        Frontend->>Librarian: Error "Book already exists"
        end
    else
        Backend-->>Frontend: Invalid code
        Frontend->>Librarian: Error "Invalid code"
    end

    Librarian-->>Frontend: Enter book info
    Frontend->>Backend: Send "add book" request
    Backend->>+MongoDB: Add book to DataBase
    MongoDB-->>-Backend: Request successful
    Backend-->>-Frontend: DataBase updated
    Frontend->>-Librarian: "Book successfully added"
```

### Sequence Diagram: Proposed

```mermaid
sequenceDiagram
actor Librarian
    Librarian->>+Frontend: Enter code
    Frontend->>+Backend: Verify code

    alt
        Backend-->>Frontend: Valid code
        Frontend->>Backend: Verify if exists
        Backend->>+MongoDB: Verify similarities

        alt
        MongoDB-->>Backend: No similarities
        Backend-->>Frontend: Book doesn't exist
        Frontend->>Librarian: Request book info

        else
        MongoDB-->>-Backend: Similarities
        Backend-->>Frontend: Book exists
        Frontend->>Librarian: Error "Book already exists"
        end
    else
        Backend-->>Frontend: Invalid code
        Frontend->>Librarian: Request book name
    end

    Librarian-->>Frontend: Enter book name
    Frontend->>Backend: Verify if exists
    Backend->>+MongoDB: Verify similarities

        alt
        MongoDB-->>Backend: No similarities
        Backend-->>Frontend: Book doesn't exist
        Frontend->>Librarian: Request book info

        else
        MongoDB-->>-Backend: Similarities
        Backend-->>Frontend: Book exists
        Frontend->>Librarian: Error "Book already exists"
        end

    Librarian-->>Frontend: Enter book info
    Frontend->>Backend: Send book infos
    Backend->>+MongoDB: Add book to DataBase
    MongoDB-->>-Backend: Request successful
    Backend-->>-Frontend: DataBase updated
    Frontend->>-Librarian: "Book successfully added"
```
