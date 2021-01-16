<template>
  <div>
    <p class="text-xl">실험에 참여해 주셔서 감사합니다!</p>
    <br />
    <p class="px-5">
      발급받은 피험자 번호와 성함을 입력 후 <br />
      시작 버튼을 클릭해 주세요
    </p>
    <hr class="border-1 w-full my-4" />
    <register-form />
  </div>
</template>

<script setup>
import RegisterForm from "../components/RegisterForm.vue";
</script>

<style scoped></style>
