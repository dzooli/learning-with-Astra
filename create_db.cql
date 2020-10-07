use usercomments;
create table comments.facebook (
    user_name text, 
    comment_time timeuuid, 
    comment_text text, 
    primary key (user_name)
);
