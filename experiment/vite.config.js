import vue from "@vitejs/plugin-vue";

/**
 * @type {import('vite').UserConfig}
 */
export default {
  plugins: [vue()],
  build: {
    manifest: true,
    rollupOptions: {
      input: "src/main.js",
    },
    base: "/static/",
  },
  server: {
    proxy: {
      "/api": {
        target: "http://127.0.0.1:8000/api",
        rewrite: (path) => path.replace(/^\/api/, ""),
      },
      "/static/stims": {
        target: "http://127.0.0.1:8000/static/stims",
        rewrite: (path) => path.replace(/^\/static\/stims/, ""),
      },
    },
  },
};
