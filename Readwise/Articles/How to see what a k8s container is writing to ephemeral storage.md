# How to see what a k8s container is writing to ephemeral storage

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/uploaded_book_covers/profile_1526994/apple-touch-icon2.png)

## Metadata
- Author: [[Stack Overflow]]
- Full Title: How to see what a k8s container is writing to ephemeral storage
- Category: #articles
- Summary: Kubernetes Pods use ephemeral storage for logs and caching but can be evicted if they exceed storage limits. To monitor what files are being written, you can use specific commands to list modified files in the Pod. For ongoing changes, you can run a loop that checks for new files while monitoring their sizes.
- URL: https://stackoverflow.com/questions/71592515/how-to-see-what-a-k8s-container-is-writing-to-ephemeral-storage

## Full Document
[[Full Document Contents/Articles/How to see what a k8s container is writing to ephemeral storage.md|See full document content →]]

## Highlights
- Pods use ephemeral local storage for scratch space, caching, and logs ([View Highlight](https://read.readwise.io/read/01jrjw7qwwxv5dc11pwbby6frq))
- find / -mount -newer /proc -print ([View Highlight](https://read.readwise.io/read/01jrjw0081wa4skzwcadc123f9))
