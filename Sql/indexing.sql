
-- creating the indexes columns

-- @block
-- indexing the email address on users table
CREATE Index idx_user_email on users(Emailaddress);

-- @block
-- indexing borrowed books users' ids
CREATE Index idx_books_users on borrowed_books(user_id);
-- indexing borrowed books books' ids
CREATE Index idx_books_booksids on borrowed_books(Book_id);


-- @block
-- indexing Books
CREATE Index idx_books_name on books(Name);
-- indexing available books
CREATE Index idx_books_aveilable on books(is_available);


-- @block
-- indexing authors
CREATE Index idx_authors on authors(name);

-- @block
-- indexing categories
CREATE Index idx_books on categories(name);


-- @block
-- indexing types
CREATE Index idx_types on types(types);