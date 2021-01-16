import { createRouter, createWebHashHistory } from "vue-router";

import useExperiment from "../hooks/useExperiment";
import useHowler from "../hooks/useHowler";

import Intro from "../pages/Intro.vue";
import Run from "../pages/Run.vue";
import Emotional from "../pages/Emotional.vue";

const { getBaseSound, getRunSound, getEmotionalSound } = useExperiment();
const { createBaseSound, createRunSound, createEmotionalSound } = useHowler();

const routes = [
  {
    path: "/",
    name: "Intro",
    component: Intro,
    beforeEnter: async (to, from, next) => {
      const { result, url } = await getBaseSound();
      if (result === "ok") {
        await createBaseSound(url);
        next();
      }
    },
  },
  {
    path: "/run",
    name: "Run",
    component: Run,
    beforeEnter: async (to, from, next) => {
      const { result, url } = await getRunSound();
      if (result === "ok") {
        await createRunSound(url);
        next();
      } else if (result === "end") {
        // TODO: next("/end");
        next("/");
      } else if (result === "error") {
        next("/");
      }
    },
  },
  {
    path: "/emotional",
    name: "Emotional",
    component: Emotional,
    beforeEnter: async (to, from, next) => {
      const { result, url } = await getEmotionalSound();
      if (result === "ok") {
        await createEmotionalSound(url);
        next();
      } else if (result === "end") {
        // Redirect to the new run
        next("/run");
      } else if (result === "error") {
        next("/");
      }
    },
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
