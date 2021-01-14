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
};
