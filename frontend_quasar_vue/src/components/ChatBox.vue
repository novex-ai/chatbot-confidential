<template>
    <div
        class="chatbox q-pa-md q-gutter-md column flex-center"
    >
        <div class="message-container q-pa-md q-ma-none bg-white shadow-1">
            <div
                class="message-window"
            >
                <q-chat-message
                    label="Sunday, 19th"
                />
                <q-chat-message
                    :text="['hey, how are you?']"
                    sent
                    stamp="7 minutes ago"
                />
                <q-chat-message
                    :text="['doing fine, how are you?']"
                    stamp="4 minutes ago"
                />
            </div>
        </div>

        <div class="input-container row q-ma-md">
            <q-input
                v-model.trim="message"
                filled
                flat
                dense
                placeholder="Type a message..."
                class="col q-mr-sm shadow-1"
            />
            <q-btn
                unelevated
                text-color="blue-10"
                icon="send"
                class="col-1"
                :disable="!message"
            />
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const message = ref<string>('');
</script>

<style lang="scss">
.chatbox {
    width: 100%;

    .message-container {
        width: 100%;
        max-width: 600px;
    }
    .message-window {
        width: 100%;
    }
    .input-container {
        width: 100%;
        max-width: 600px;
    }
}
</style>
