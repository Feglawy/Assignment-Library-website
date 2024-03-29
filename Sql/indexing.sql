
-- creating the indexes columns

-- @block
-- indexing the email address on users table
CREATE Index idx_user_email on library.users(Emailaddress);

-- @block
-- indexing borrowed books users' ids
CREATE Index idx_books_users on library.borrowed_books(user_id);
-- @block
-- indexing borrowed books books' ids
CREATE Index idx_books_booksids on library.borrowed_books(Book_id);


-- @block
-- indexing Books
CREATE Index idx_books_name on library.books(Name);
-- @block
-- indexing available books
CREATE Index idx_books_aveilable on library.books(is_available);


-- @block
-- indexing authors
CREATE Index idx_authors on library.authors(name);

-- @block
-- indexing categories
CREATE Index idx_books on library.categories(name);


-- @block
-- indexing types
CREATE Index idx_types on library.types(types);