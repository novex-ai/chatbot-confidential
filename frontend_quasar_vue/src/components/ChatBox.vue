<template>
    <div
        class="chatbox q-pa-md q-gutter-md column flex-center bg-grey-2"
    >
        <div class="message-container q-pa-md q-ma-none bg-white">
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
      
    <div>Input</div>
  </div>
</template>

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
}
</style>
