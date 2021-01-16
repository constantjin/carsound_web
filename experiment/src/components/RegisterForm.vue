<template>
  <form class="mt-5 px-10" @submit="false">
    <label for="id" class="block text-base font-semibold text-black">
      피험자 번호
    </label>
    <input
      id="id"
      type="number"
      placeholder="피험자 번호(숫자)"
      class="block w-full h-10 text-center mt-2 text-black border-b-2"
      v-model="state.subject_id"
    />
    <br />
    <label for="name" class="block text-base font-semibold text-black">
      성함
    </label>
    <input
      id="name"
      type="text"
      placeholder="성함"
      class="block w-full h-10 text-center mt-2 text-black border-b-2"
      v-model="state.name"
    />
    <br />
    <button
      class="h-10 mt-5 px-6 text-base font-semibold border-2"
      @click.prevent="submitForm"
    >
      {{ button_text }}
    </button>
  </form>
</template>

<script setup>
import { reactive, ref } from "vue";
import { useRouter } from "vue-router";

import useExperiment from "../hooks/useExperiment";
import useError from "../hooks/useError";

const router = useRouter();

const state = reactive({
  subject_id: null,
  name: null,
});
const button_text = ref("실험 시작");

const { registerSubject, isRegistered, getBaseSound } = useExperiment();
const { showError, resetError } = useError();

const checkInt = (str) => {
  return /^\+?\d+$/.test(str);
};

const checkForm = () => {
  if (!(state.subject_id && state.name)) {
    // Check empty fields
    showError("ID 또는 성함을 입력해 주세요");
    return false;
  } else if (!checkInt(state.subject_id)) {
    showError("ID에는 숫자를 입력해 주세요");
    return false;
  } else {
    resetError();
    return true;
  }
};

const submitForm = async () => {
  if (checkForm()) {
    await registerSubject(state);
    if (isRegistered()) {
      button_text.value = "로딩 중..";
      router.push("/run");
    }
  }
};
</script>

<style scoped></style>
