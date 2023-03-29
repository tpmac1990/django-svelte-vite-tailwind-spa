<script>
    import { onMount } from "svelte";

    export let fetchBlogs;

    let blogs = [];
    let resp;

    async function loadBlogs() {
        resp = await fetchBlogs();
        blogs = resp.blogs;
    }

    onMount(loadBlogs);
</script>

<h1>Blog List</h1>
<ul>
    {#each blogs as blog}
        <li><a href={`blogs/${blog.id}`}>{blog.title}</a></li>
    {/each}
</ul>
