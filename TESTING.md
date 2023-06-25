# Table of content
- [User stories tests](#user-stories-tests)
- [Model tests, CRUD operations, input validation, relationships, logic](#model-tests-crud-operations-input-validation-relationships-logic)
- [PEP8 Validation](#pep8-validation)

<hr>

# User stories tests

| User story   | Test Result |
|--------------|-------------|
| As a user, I want to be able to create a profile, so I can provide information about myself. | PASS |
| As a user, I want to be able to edit my profile, so I can update my name, bio, and Instagram handle. | PASS |
| As a user, I want to be able to upload an image for my profile picture, so I can personalize my profile. | PASS |
| As a user, I want my profile to display the date and time it was created and edited so I can see when my profile was established and updated. | PASS |
| As a user, I want my default profile picture to be set if I haven't uploaded a custom image, so my profile always has an image present. | PASS |
| As a site admin, I want profiles to be automatically created when users sign up for an account, so I don't have to manually create it. | PASS |
| As a user, I want to be able to create a new post by providing a title, category, optional EXIF data, post content, and an image. | PASS |
| As a user, I want to be able to view the details of a specific post, including its title, category, creation time, and other optional fields. | PASS |
| As a user, I want to be able to update my posts and be able to delete them. | PASS |
| As a user, I want to be able to filter posts by provided fields, so that I can see posts related to specific criteria. | PASS |
| As a user, I want to be able to search for posts by their title or content, so that I can find posts that contain specific keywords. | PASS |
| As a user, I want to be able to upload an image for a post and have it displayed along with other post details. | PASS |
| As a user, I want to be able to add a comment to a specific post. | PASS |
| As a user, I want to be able to edit the comments that I have posted. | PASS |
| As a user, I want to be able to delete a comment that I have posted. | PASS |
| As a user, I want to be able to see the total number of comments I have posted. | PASS |
| As a user, I want to be able to view the details of a specific comment, including its content, creation time, and the associated post. | PASS |
| As a user, I can post a "like" or remove it for a specific post. | PASS |
| As a user, I can view the list of likes that posts received with details such as users who added likes, and time added. | PASS |
| As a user, I want to be able to follow other users and see who is following me. | PASS |
| As a user, I want to be able to see how many users follow me, and also how many users I follow, so I can keep track of the popularity of my profile. | PASS |

User story marked as possible future enchancement: 

| User story   | Comment |
|--------------|-------------|
| As a user I want to be able to add tags to my posts and be able to display tagged posts so I can easily find the content that I'm interested in. | Adding tags is possible, they are stored as a string with comma-separated words. Adding separate tags with many-to-many relations has beed marked as possible future enchancement. That would allow for e.g. searching tagged posts |


# Model tests (CRUD operations, input validation, relationships, logic)

## Profiles app

| Test Description                                | Steps                                                                           | Expected Result | Test result |
|-------------------------------------------------|---------------------------------------------------------------------------------|-----------------|-------------|
| Create a new profile                            | Register a new user through admin and verify that a profile is automatically created | Profile is successfully created and associated with the user | PASS |
| Test optional fields                            | Create new user as admin                                                        | Profile is successfully created with blank optional fields | PASS |
| View profile details                            | Open the profile details endpoint with specific user ID                         | Profile details: name, bio, equipment, instagram, image, are displayed | PASS |
| Update profile                                  | As prfile owner, modify the fields and submit the form                          | Profile information is successfully updated with the new data | PASS |
| Update profile image                            | As profile owner, upload new image and submit the form                          | Profile image is successfully updated with the new image | PASS |
| Test profile image validation                   | As profile owner, upload new image exceeding allowed height, width and file size (2500px, 2500px, 2MB respectively) | Profile image change is denied and appropriate message is displayed | PASS |
| View a list of profiles                         | Open /profiles endpoint                                                         | All existing profiles are displayed in descending order of creation date | PASS |
| Test character limits for fields                | Create a profile with fields exceeding their maximum character limits           | Appropriate validation error messages are displayed | PASS |

## Posts app

| Test Description                                | Steps                                                                           | Expected Result | Test result |
|------------------------------------------------ |---------------------------------------------------------------------------------|-----------------|-------------|
| Create a new post                               | Log in, fill the form and submit the form                                       | Post is successfully created and displayed on the post list page | PASS |
| View a list of posts                            | Open the /posts list page                                                       | All existing posts are displayed in descending order of creation date | PASS |
| View details of a specific post                 | Open the post detail page e.g. /posts/1                                         | Post details, including title, category, tags, and image are displayed | PASS |
| Update an existing post                         | As the post owner, modify the fields and submit the form                        | Post is successfully updated with the new data | PASS |
| Delete an existing post                         | As the post owner, in post detail view, click delete post and confirm           | Post is successfully deleted and removed from the post list page | PASS |
| Create a post without providing an image        | Log in, create post without uploading the image and submit the form             | Post is successfully created without custom image, default image is present | PASS |
| Create a post with an image                     | Log in, create post with custom image and suubmit the form                      | Post is successfully created with the custom image and displayed on the post list page | PASS |
| View a list of posts with applied category filter | On post list page, filter posts by category                                   | Only posts with filtered characteristic are displayed | PASS |
| Test search option                              | Search posts by entering post title, category and post owner                    | Only posts with searched characteristic are displayed | PASS |
| Test pagination                                 | Create at least 11 posts and check if  pagination works                         | Posts are displayed with pagination, showing 10 posts per page | PASS | 
| Test ordering of posts                          | Open the post list page and check list order                                    | Posts are displayed in descending order based on their creation dates | PASS |
| Test validation                                 | Create a post and leave required fields empty, submit the form                  | Appropriate validation error messages are displayed | PASS |
| Test character limits for fields                | Create a post with fields exceeding their maximum character limits, submit      | Appropriate validation error messages are displayed | PASS |
| Test optional fields                            | Create a post without filling in optional fields, submit the form               | Post is successfully created with blank optional fields | PASS |
| Test updating an image for an existing post     | As the post owner, open post details and submit the form with changed image     | Post is successfully updated with the new image | PASS |
| Test post image validation                      | As profile owner, upload new image exceeding allowed height, width and file size (2500px, 2500px, 2MB respectively) | Post image change is denied and appropriate message is displayed | PASS |

## Comments

| Test Description                                | Steps                                                                           | Expected Result | Test result |
|-------------------------------------------------|---------------------------------------------------------------------------------|-----------------|-------------|
| Create a new comment                            | Log in, open a post detail page, write a comment, submit the form               | Comment is successfully created and displayed on the post detail page | PASS |
| View a list of all comments using filter        | Open /comment endpoint, use filter to select post                               | All comments for selected post are displayed | PASS |
| View a list of comments for a post              | Open comment detail page for specific post e.g /comments/1                      | All comments for the specific post are displayed in descending order of creation date | PASS |
| Edit an existing comment                        | As comment owner, modify comment, submit the form                               | Comment content is successfully updated with the new content | PASS |
| Delete an existing comment                      | As comment owner, open comment details page, delete it and confirm the deletion | Comment is successfully deleted and removed from the post detail page and comments list | PASS |
| Test ordering of comments                       | Create multiple comments for a post, open comments list and details page        | Comments are displayed in descending order based on their creation dates on both pages | PASS |
| Test validation                                 | Create a comment without entering any content, submit the form                  | Appropriate validation error message is displayed | PASS |
| Test character limits for comment content       | Create a comment exceeding the maximum character limit, submit the form         | Appropriate validation error message is displayed | PASS |
| Test unauthorized deletion                      | Log in as a different user than owner, attempt to delete a comment belonging to another user | Deletion is not available for unauthorized user |  PASS |
| Test comments count                             | Check /posts list view and post detailed view if comments count displays correct value | Comments count is displayed in both views and shows correct value | PASS | 

## Likes

| Test Description                                | Steps                                                                           | Expected Result | Test result |
|-------------------------------------------------|---------------------------------------------------------------------------------|-----------------|-------------|
| Like a post                                     | Log in, open /likes page, add like to any post, send the form                   | Like is successfully created for the post | PASS |
| Unlike a post                                   | As the user who previously liked the post, delete like on like/id page, send form| Like is successfully removed from the post | PASS |
| Test ordering of likes                          | Create multiple likes for a post with different creation dates<br>2. Open the post detail page | Likes are displayed in descending order based on their creation dates | PASS |
| Test unauthorized liking and unliking           | Attempt to like or unlike a post while not being logged in                      | Like form is not available | PASS |
| Test unique liking per user per post            | Log in, like a post, attempt to like the same post again                        | Second like request is denied and and "possible duplicate" message is displayed | PASS | 
| Test likes count                                | Check /posts list view and post detailed view if likes count displays correct value | Likes count is displayed in both views adn shows correct value | PASS | 

## Followers

| Test Description                                | Steps                                                                               | Expected Result | Test result |
|-------------------------------------------------|-------------------------------------------------------------------------------------|-----------------|-------------|
| Follow a user                                   | Log in, open the followers endpoint, select user to follow and submit the form | User is successfully followed by the currently logged-in user | PASS |
| Unfollow a user                                 | Log in as the user who is following the other user, open followers detail page with specific id, select following user and submit| User is successfully unfollowed by the logged-in user who previously followed this user | PASS |
| View users followed by a user                   | Open the followers endpoint page and check relation between profile id and followed value | The list displays correct followed and followed_name values for specific profile id | PASS |
| Test ordering of followers and followed users   | Create multiple follower relationships, open followers endpoint                  | Follower list is displayed in descending order based on follows creation dates | PASS |
| Test unauthorized following and unfollowing     | As unauthorized user attempt to follow any user                                  | Follow or unfollow is not available | PASS |
| Test "unique_together" relationship             | Log in, follow specific user and attempt to follow the same user again           | Second follow request is denied and "possible duplicate" message is displayed | PASS |
| Test followers and followint count              | Check /profile list view and profile detailed view if followers count and following count display correct values | Followers and following count are displayed in both views and shows correct values | PASS | 

# PEP8 Validation

All files has been linted using [PEP8 Linter](https://pep8ci.herokuapp.com/) created by Code Institute. 

Minor mistakes such as trailing whitespaces, double empty line between classes or missing empty line at the end of the file, have been corrected, all warnings haved been cleared out.

Syntax and indentation errors were fixed in the IDE as they arises during development stage.

Please note that settings.py file includes couple of lines that are too long but breaking them would cause fail in heroku deployment. This is third party django code. 