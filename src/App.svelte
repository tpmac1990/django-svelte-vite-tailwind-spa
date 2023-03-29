<script>
    import { Router, Route } from "svelte-navigator";
    import BlogList from "./components/BlogList.svelte";
    import BlogDetail from "./components/BlogDetail.svelte";

    const API_BASE_URL = "http://localhost:8000/api"; // our Django API base URL

    function fetchBlogs() {
        return fetch(`${API_BASE_URL}/blogs/`).then((res) => res.json());
    }

    function fetchBlog(id) {
        return fetch(`${API_BASE_URL}/blogs/${id}/`).then((res) => res.json());
    }
</script>

<Router>
    <Route path="/">
        <BlogList {fetchBlogs} />
    </Route>
    <Route path="/blogs/:id">
        <BlogDetail {fetchBlog} />
    </Route>
</Router>
