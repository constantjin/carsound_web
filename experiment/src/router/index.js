import { createRouter, createWebHashHistory } from "vue-router";

import useExperiment from "../hooks/useExperiment";
import useHowler from "../hooks/useHowler";

import Intro from "../pages/Intro.vue";
import Run from "../pages/Run.vue";
import Emotional from "../pages/Emotional.vue";
import Rating from "../pages/Rating.vue";
import End from "../pages/End.vue";
import Error from "../pages/Error.vue";

const { getBaseSound, getRunSound, getEmotionalSound } = useExperiment();
const {
  createBaseSound,
  createRunSound,
  createEmotionalSound,
  pauseBaseSound,
  destroyBaseSound,
  destroyRunSound,
} = useHowler();

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
        destroyBaseSound();
        next("/end");
      } else if (result === "error") {
        next("/error");
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
        destroyRunSound();
        pauseBaseSound();
        next("/run");
      } else if (result === "error") {
        next("/error");
      }
    },
  },
  {
    path: "/rating",
    name: "Rating",
    component: Rating,
  },
  {
    path: "/end",
    name: "End",
    component: End,
  },
  {
    path: "/error",
    name: "Error",
    component: Error,
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
