import { reactive, toRefs } from "vue";
import axios from "axios";

import useError from "./useError";

const registerApi = "/api/register/";
const baseSoundApi = "/api/get-base/";
const runSoundApi = "/api/get-run/";
const emotionalSoundApi = "/api/get-emotional/";

const { showError, resetError } = useError();

const experiment = reactive({
  subject_pk: null,
  run_pk: null,
  emotional_pk: null,
});

export default function useExperiment() {
  // Hooks for registering subjects
  const registerSubject = async ({ name, subject_id }) => {
    try {
      experiment.subject_pk = null;
      const response = await axios.post(registerApi, {
        subject_id,
        name,
      });
      experiment.subject_pk = response.data.id;
      console.log(
        `-- DEBUG -- \nregisterd subject_pk:\n  ${experiment.subject_pk}`
      );
      resetError();
    } catch (err) {
      experiment.subject_pk = null;
      const status_code = err.response.status;
      if (status_code === 400) {
        showError("피험자 번호가 중복됩니다");
      } else {
        console.error(err);
        showError("서버 에러가 발생했습니다");
      }
    }
  };

  const isRegistered = () => experiment.subject_pk !== null;

  // Hooks for retrieving base sound urls
  const getBaseSound = async () => {
    let res = {
      result: null,
      url: null,
    };

    try {
      const response = await axios.get(baseSoundApi);
      res.result = "ok";
      res.url = response.data.url;
      console.log(`-- DEBUG -- \nbase sound URL:\n  ${res.url}`);
      resetError();
      return res;
    } catch (err) {
      console.error(err);
      showError("서버 에러가 발생했습니다");
      res.result = "error";
      return res;
    }
  };

  // Hooks for retrieving run sound urls
  const getRunSound = async () => {
    let res = {
      result: null,
      url: null,
    };

    try {
      const endpoint = `${runSoundApi}${experiment.subject_pk}`;
      const response = await axios.get(endpoint);
      const status_code = response.status;
      if (status_code === 204) {
        // Experiment finished
        experiment.run_pk = null;
        resetError();
        res.result = "end";
        return res;
      } else {
        experiment.run_pk = response.data.id;
        res.result = "ok";
        res.url = response.data.url;
        console.log(`-- DEBUG -- \nrun sound URL:\n  ${res.url}`);
        resetError();
        return res;
      }
    } catch (err) {
      console.error(err);
      showError("서버 에러가 발생했습니다");
      res.result = "error";
      return res;
    }
  };

  // Hooks for retrieving emotional sound urls
  const getEmotionalSound = async () => {
    let res = {
      result: null,
      url: null,
    };

    try {
      const endpoint = `${emotionalSoundApi}${experiment.subject_pk}/${experiment.run_pk}`;
      const response = await axios.get(endpoint);
      const status_code = response.status;
      if (status_code === 204) {
        // Run finished
        experiment.emotional_pk = null;
        resetError();
        res.result = "end";
        return res;
      } else {
        experiment.emotional_pk = response.data.id;
        res.result = "ok";
        res.url = response.data.url;
        console.log(`-- DEBUG -- \nemotional sound URL:\n  ${res.url}`);
        resetError();
        return res;
      }
    } catch (err) {
      console.error(err);
      showError("서버 에러가 발생했습니다");
      res.result = "error";
      return res;
    }
  };

  return {
    ...toRefs(experiment),
    registerSubject,
    isRegistered,
    getBaseSound,
    getRunSound,
    getEmotionalSound,
  };
}
