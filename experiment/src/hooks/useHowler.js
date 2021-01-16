import { reactive, toRefs } from "vue";
import { Howl } from "howler";

const sounds = reactive({
  base_sound: null,
  run_sound: null,
  emotional_sound: null,
});

export default function useHowler() {
  // Hooks for base sound controls
  const isBaseCreated = () => sounds.base_sound !== null;

  const isBasePlaying = () => isBaseCreated() && sounds.base_sound.playing();

  const createBaseSound = (url) => {
    const promise = new Promise((resolve, reject) => {
      if (isBaseCreated()) {
        resolve();
      }
      const baseHowl = new Howl({
        src: [url],
        preload: true,
        loop: true,
      });
      baseHowl.on("load", () => {
        sounds.base_sound = baseHowl;
        console.log("-- DEBUG -- \nbase sound loaded");
        resolve();
      });
    });
    return promise;
  };

  const destroyBaseSound = () => {
    if (isBaseCreated()) {
      sounds.base_sound.unload();
    }
    sounds.base_sound = null;
  };

  const playBaseSound = () => {
    if (isBaseCreated() && !isBasePlaying()) {
      console.log("-- DEBUG -- \nbase sound playing");
      sounds.base_sound.play();
    }
  };

  const pauseBaseSound = () => {
    if (isBaseCreated()) {
      sounds.base_sound.pause();
    }
  };

  // Hooks for run sound controls
  const isRunCreated = () => sounds.run_sound !== null;

  const isRunPlaying = () => isRunCreated() && sounds.run_sound.playing();

  const createRunSound = (url) => {
    const promise = new Promise((resolve, reject) => {
      if (url === "") {
        resolve();
      }
      const runHowl = new Howl({
        src: [url],
        preload: true,
        loop: true,
        volume: 0.8,
      });
      runHowl.on("load", () => {
        sounds.run_sound = runHowl;
        console.log("-- DEBUG -- \nrun sound loaded");
        resolve();
      });
    });
    return promise;
  };

  const destroyRunSound = () => {
    if (isRunCreated()) {
      sounds.run_sound.unload();
    }
    sounds.run_sound = null;
  };

  const playRunSound = () => {
    if (isRunCreated() && !isRunPlaying()) {
      console.log("-- DEBUG -- \nrun sound playing");
      sounds.run_sound.play();
    }
  };

  const stopRunSound = () => {
    if (isRunCreated()) {
      sounds.run_sound.stop();
    }
  };

  // Hooks for emotional sound controls
  const isEmotionalCreated = () => sounds.emotional_sound !== null;

  const isEmotionalPlaying = () =>
    isEmotionalCreated() && sounds.emotional_sound.playing();

  const createEmotionalSound = (url) => {
    const promise = new Promise((resolve, reject) => {
      const emotionalHowl = new Howl({
        src: [url],
        preload: true,
      });
      emotionalHowl.on("load", () => {
        sounds.emotional_sound = emotionalHowl;
        console.log("-- DEBUG -- \nemotional sound loaded");
        resolve();
      });
    });
    return promise;
  };

  const destroyEmotionalSound = () => {
    if (isEmotionalCreated()) {
      sounds.emotional_sound.unload();
    }
    sounds.emotional_sound = null;
  };

  const playEmotionalSound = () => {
    if (isEmotionalCreated() && !isEmotionalPlaying()) {
      const promise = new Promise((resolve, reject) => {
        console.log("-- DEBUG -- \nemotional sound playing");
        sounds.emotional_sound.play();
        sounds.emotional_sound.on("end", () => {
          console.log("-- DEBUG -- \nemotional sound ended");
          resolve();
        });
      });

      return promise;
    }
  };

  return {
    ...toRefs(sounds),
    createBaseSound,
    destroyBaseSound,
    playBaseSound,
    pauseBaseSound,
    isBaseCreated,
    isBasePlaying,
    createRunSound,
    destroyRunSound,
    playRunSound,
    stopRunSound,
    createEmotionalSound,
    destroyEmotionalSound,
    playEmotionalSound,
  };
}
