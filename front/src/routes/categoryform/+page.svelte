<script>
    import { createCategory } from "$lib/api.js";
    import { goto } from "$app/navigation";

    let name = "";
    let slug = "";

    async function handleSubmit() {
        await createCategory({ name, slug });
        goto("/");
    }
</script>

<h2>New Category</h2>
<form on:submit|preventDefault={handleSubmit}>
    <input bind:value={name} placeholder="Name" required />
    <input bind:value={slug} placeholder="Slug" required />
    <button type="submit">Create</button>
</form>
