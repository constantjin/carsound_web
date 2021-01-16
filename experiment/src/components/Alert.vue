<template>
  <transition name="slide-fade">
    <div
      v-if="error_msg"
      class="flex flex-row bg-red-100 border border-red-200 text-red-700 pl-4 pr-8 py-3 rounded -mb-6"
      role="alert"
    >
      <strong class="font-bold mr-5">에러</strong>
      <span class="block sm:inline">{{ error_msg }}</span>
    </div>
  </transition>
</template>

<script setup>
import useError from "../hooks/useError";

const { error_msg } = useError();
</script>

<style scoped>
.slide-fade-enter-active,
.slide-fade-leave-active {
  transition: opacity 0.4s ease;
}
.slide-fade-enter-from,
.slide-fade-leave-to {
  opacity: 0;
}
</style>
