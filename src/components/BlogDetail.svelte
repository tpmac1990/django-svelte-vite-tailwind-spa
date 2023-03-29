<script>
    import { onMount } from "svelte";
    export let fetchBlog;

    let blog = {};
    // extract the page id from the url
    const url = window.location.href;
    const sp = url.split("/");
    const id = sp[sp.length - 2];

    async function loadBlog() {
        const resp = await fetchBlog(id);
        blog = resp.blog;
    }

    onMount(loadBlog);
</script>

<h1>{blog.title}</h1>
<p>{blog.content}</p>
