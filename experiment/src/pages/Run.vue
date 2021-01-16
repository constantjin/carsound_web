<template>
  <div>
    <p class="text-xl">조금 뒤 실험이 시작됩니다</p>
    <hr class="border-1 w-full my-4" />
    <ul class="text-left space-y-3">
      <li><span>🔈</span> 이어폰으로 들리는 소리에 <b>집중</b>해 주세요</li>
      <li><span>✔️</span> 응답은 <b>빠르고 정확하게</b> 해 주세요</li>
      <li><span>⏱️</span> <b>10초</b>간 미응답시 자동으로 넘어갑니다</li>
    </ul>
  </div>
</template>

<script setup>
import { onMounted } from "vue";
import { useRouter, onBeforeRouteLeave } from "vue-router";

import useHowler from "../hooks/useHowler";

const router = useRouter();
const { playBaseSound, playRunSound } = useHowler();

onMounted(() => {
  onBeforeRouteLeave((to, from) => {
    if (to.name === "Emotional") {
      playBaseSound();
      playRunSound();
    }
  });

  setTimeout(() => {
    router.push("/emotional");
  }, 3000);
});
</script>

<style scoped></style>
