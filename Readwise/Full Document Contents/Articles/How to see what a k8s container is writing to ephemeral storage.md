# How to see what a k8s container is writing to ephemeral storage

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/uploaded_book_covers/profile_1526994/apple-touch-icon2.png)

## Metadata
- Author: [[Stack Overflow]]
- Full Title: How to see what a k8s container is writing to ephemeral storage
- Category: #articles
- Summary: Kubernetes Pods use ephemeral storage for logs and caching but can be evicted if they exceed storage limits. To monitor what files are being written, you can use specific commands to list modified files in the Pod. For ongoing changes, you can run a loop that checks for new files while monitoring their sizes.
- URL: https://stackoverflow.com/questions/71592515/how-to-see-what-a-k8s-container-is-writing-to-ephemeral-storage

## Full Document
Adding details to the topic.

>  Pods use ephemeral local storage for scratch space, caching, and logs. **Pods can be evicted due to other pods filling the local storage, after which new pods are not admitted until sufficient storage has been reclaimed.**
> 
>  

The kubelet can provide scratch space to Pods using local ephemeral storage to mount [emptyDir](https://kubernetes.io/docs/concepts/storage/volumes/#emptydir) volumes into containers.

* For container-level isolation, if a container's writable layer and log usage exceeds its storage limit, the kubelet marks the Pod for eviction.
* For pod-level isolation the kubelet works out an overall Pod storage limit by summing the limits for the containers in that Pod. In this case, if the sum of the local ephemeral storage usage from all containers and also the Pod's emptyDir volumes exceeds the overall Pod storage limit, then the kubelet also marks the Pod for eviction.

To see what files have been written since the pod started, you can run:

```
find / -mount -newer /proc -print

```

This will output a list of files modified more recently than '/proc'.

```
/etc/nginx/conf.d
/etc/nginx/conf.d/default.conf
/run/secrets
/run/secrets/kubernetes.io
/run/secrets/kubernetes.io/serviceaccount
/run/nginx.pid
/var/cache/nginx
/var/cache/nginx/fastcgi_temp
/var/cache/nginx/client_temp
/var/cache/nginx/uwsgi_temp
/var/cache/nginx/proxy_temp
/var/cache/nginx/scgi_temp
/dev

```

Also, try without the '-mount' option.

To see if any new files are being modified, you can run some variations of the following command in a Pod:

```
while true; do rm -f a; touch a; sleep 30; echo "monitoring..."; find / -mount -newer a -print; done

```

and check the file size using the `du -h someDir` command.

Also, as @gohm'c pointed out in his answer, you can use sidecar/ephemeral debug containers.

Read more about [Local ephemeral storage here](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#local-ephemeral-storage).
