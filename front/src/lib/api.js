const base = import.meta.env.VITE_API_URL || "http://localhost:8000";
const API_URL = `${base}/api`;
export async function getPosts() {
  const res = await fetch(`${API_URL}/posts/`);
  return await res.json();
}

export async function getPost(id) {
  const res = await fetch(`${API_URL}/posts/${id}`);
  return await res.json();
}

export async function getCategories() {
  const res = await fetch(`${API_URL}/categories/`);
  return await res.json();
}

export async function getCategoryPosts(slug) {
  const res = await fetch(`${API_URL}/categories/${slug}`);
  return await res.json();
}

export async function createPost(data) {
  const res = await fetch(`${API_URL}/posts/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  return await res.json();
}

export async function updatePost(id, data) {
  const res = await fetch(`${API_URL}/posts/${id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  return await res.json();
}

export async function deletePost(id) {
  await fetch(`${API_URL}/posts/${id}`, { method: "DELETE" });
}

export async function getComments(postId) {
  const res = await fetch(`${API_URL}/comments/post/${postId}`);
  return await res.json();
}

export async function addComment(data) {
  const res = await fetch(`${API_URL}/comments/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  return await res.json();
}
