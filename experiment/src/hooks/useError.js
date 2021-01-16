import { reactive, toRefs } from "vue";

const error = reactive({
  error_msg: "",
});

export default function useError() {
  const showError = (msg) => {
    error.error_msg = msg;
  };

  const resetError = () => {
    error.error_msg = "";
  };

  return {
    ...toRefs(error),
    showError,
    resetError,
  };
}
