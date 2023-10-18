<template>
    <q-page class="column items-center justify-start">
      <q-form
        greedy
        @submit="onSubmit"
        @reset="onReset"
        class="q-ma-none"
      >
        <q-input
          v-model.trim="chat_prompt_template"
          outlined
          :rules="chat_prompt_template_rules"
          label="Chat Prompt Template"
          type="textarea"
          class="q-ma-none"
          style="width: 400px; height: 180px;"
          rows="8"
          spellcheck="true"
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

const chat_prompt_template = ref<string>(`
You are a helpful assistant who knows about the following context: \${context}.
###
\${message}
`)

const chat_prompt_template_rules = [
  (val: string) => !!val || 'Required',
  (val: string) => val.includes('${context}') || 'Must include ${context}',
  (val: string) => val.includes('${message}') || 'Must include ${message}',
]

function onSubmit() {
  console.log('submit')
}

function onReset() {
  console.log('reset')
}
</script>