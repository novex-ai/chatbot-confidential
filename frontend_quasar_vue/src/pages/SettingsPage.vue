<template>
    <q-page class="row items-center justify-evenly">
      <q-form
        @submit="onSubmit"
        @reset="onReset"
        class="q-gutter-md"
      >
        <q-input
          v-model="chat_prompt_template"
          outlined
          label="Chat Prompt Template"
          type="textarea"
          style="width: 400px; height: 400px;"
        />
        <div class="row">
          <q-btn
            type="reset"
            label="Cancel"
            class="q-ma-md"
          />
          <q-space />
          <q-btn
            type="submit"
            label="Submit"
            color="primary"
            class="q-ma-md"
          />
        </div>
      </q-form>
    </q-page>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const chat_prompt_template = ref(`
You are a helpful assistant who knows about the following context: \${context}.
###
\${message}
`)

function onSubmit() {
  console.log('submit')
}

function onReset() {
  console.log('reset')
}
</script>