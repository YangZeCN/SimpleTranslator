<template>
  <el-card class="container">
    <h2>SimpleTranslator - 翻译小助手</h2>

    <!-- Agent Config -->
    <el-form :model="currentAgent" label-width="100px" class="section">
      <el-form-item label="API提供商">
        <el-select v-model="currentAgentProvider" placeholder="请选择" @change="onProviderChange">
          <el-option v-for="agent in agentList" :key="agent.provider" :label="agent.provider" :value="agent.provider" />
        </el-select>
      </el-form-item>
      <el-button type="primary" @click="openEditAgent" v-if="shouldShowEditAgent">Update Agent</el-button>
      <!-- <el-input v-model="currentAgent.provider" v-if="currentAgent"/> -->
    </el-form>

    <!-- Model Config -->
    <el-form :model="currentModel" label-width="100px" class="section">
      <el-form-item label="Model" v-if="currentModel && currentModel?.name && appConfig">
        <el-select v-model="currentModelName" placeholder="请选择" @change="onModelChange">
          <el-option v-for="llmModel in filterModelsByProvider" :key="llmModel.name" :label="llmModel.name" :value="llmModel.name" />
        </el-select>
      </el-form-item>
      <!-- <el-input v-model="currentModel.name" v-if="currentModel"/> -->
    </el-form>

    <!-- 功能模式 -->
    <el-radio-group v-model="mode" class="section">
      <el-radio label="translate">翻译</el-radio>
      <el-radio label="polish">英文润色</el-radio>
      <el-radio label="email">邮件撰写</el-radio>
      <el-radio label="chat">自由对话</el-radio>
    </el-radio-group>

    <!-- 输入区域 -->
    <el-form class="section">
      <el-form-item label="输入">
        <el-input type="textarea" v-model="inputText" rows="6" />
      </el-form-item>
      <el-form-item label="目标语言">
        <el-select v-model="targetLang" placeholder="请选择">
          <el-option label="中文" value="zh" />
          <el-option label="英文" value="en" />
        </el-select>
      </el-form-item>
      <el-button-group>
        <el-button @click="pasteText">粘贴</el-button>
        <el-button @click="clearInput">清空</el-button>
        <el-button type="primary" @click="processText">处理</el-button>
      </el-button-group>
    </el-form>

    <!-- 输出区域 -->
    <el-form class="section">
      <el-form-item label="输出">
        <el-input type="textarea" v-model="outputText" rows="6" readonly />
      </el-form-item>
      <el-button-group>
        <el-button @click="copyOutput">复制结果</el-button>
        <el-button @click="clearOutput">清空输出</el-button>
      </el-button-group>
    </el-form>
  </el-card>

  
  <!-- Update Agent -->
  <el-dialog title="Update Agent" v-model="editAgentVisible">
    <el-form :model="currentAgent" v-if="currentAgent" class="device-form">
      <el-form-item label="Provider">
        <el-input v-model="currentAgent.provider" disabled/>
      </el-form-item>
      <el-form-item label="API Key">
        <el-input v-model="currentAgent.api_key" type="password" show-password />
      </el-form-item>
      <el-form-item label="Base Url">
        <el-input v-model="currentAgent.base_url" />
      </el-form-item>
      <el-form-item label="Description">
        <el-input v-model="currentAgent.description" />
      </el-form-item>
    </el-form>
    <template #footer>
      <el-button @click="editAgentVisible = false">Cancel</el-button>
      <el-button type="primary" @click="updateAgent">Save</el-button>
    </template>
  </el-dialog>
</template>

<script lang="ts" setup>
import axios from 'axios'
import { computed, onMounted, ref } from 'vue'
import { ElMessage, ElMessageBox } from 'element-plus'

const currentAgent = ref(null)

const appConfig = ref(null)
const currentModel = ref(null)

const currentAgentProvider = ref('')
const currentModelName = ref('')

const editAgentVisible = ref(false)


const agentList = ref([])

const mode = ref('translate')
const inputText = ref('')
const outputText = ref('')
const targetLang = ref('zh')


function pasteText() {
  navigator.clipboard.readText().then(text => {
    inputText.value = text
  })
}

function clearInput() {
  inputText.value = ''
}

const processText = async () => {
  if (!inputText.value.trim()) {
    ElMessage.warning('请输入文本')
    return
  }
  if (!currentAgent.value || !currentModel.value) {
    ElMessage.warning('请先配置API提供商和模型')
    return
  }

  let prompt = inputText.value

  try {
    const response = await axios.post('/api/translate', {
      prompt: prompt,
      provider: currentAgent.value.provider,
      model: currentModel.value.name,
      mode: mode.value,
      target_lang: targetLang.value
    })
    if (response.status !== 200) {
      ElMessage.error('处理文本失败，请稍后重试', response.data.message || '')
      return
    }
    outputText.value = response.data.result
  } catch (error) {
    console.error('Translation error:', error)
    ElMessage.error('处理文本时出错，请稍后重试')
  }
}

function copyOutput() {
  navigator.clipboard.writeText(outputText.value)
}

function clearOutput() {
  outputText.value = ''
}

const openEditAgent = () => {
  editAgentVisible.value = true
}

const loadAgentConfigs = async () => {
  try {
    const res = await axios.get('/api/agents')
    console.log('Agent Configs:', res.data)
    agentList.value = res.data
    if (null === currentAgent.value && agentList.value.length > 0) {
      console.log('Setting currentAgent to first agent:', agentList.value[0])
      currentAgent.value = agentList.value[0]
      currentAgentProvider.value = currentAgent.value.provider
      console.log('Current Agent Provider set to:', currentAgentProvider.value)
    }
  } catch (error) {
    console.error('Failed to load agent configs:', error)
    ElMessage.error('Loading agent configurations failed.')
  }
}

const loadAppConfig = async () => {
  try {
    const res = await axios.get('/api/config')
    console.log('App Config:', res.data)
    // You can use the app config data as needed
    appConfig.value = res.data
    if (appConfig.value && appConfig.value.models && appConfig.value.models.length > 0) {
      currentModel.value = appConfig.value.models[0]
      currentModelName.value = currentModel.value.name
      console.log('Current Model set to:', currentModel.value)
    }
  } catch (error) {
    console.error('Failed to load app config:', error)
    ElMessage.error('Loading app configuration failed.')
  }
}

const updateAgent = async () => {
  try {
    await axios.put(`/api/agents/${currentAgent.value.id}`, currentAgent.value)
    ElMessage.success('Agent updated successfully')
    editAgentVisible.value = false
    loadAgentConfigs()
    editAgentVisible.value = false
    ElMessage.success('Agent updated successfully')
  } catch (error) {
    console.error('Failed to update agent:', error)
    ElMessage.error('Failed to update agent')
  }
}

const onProviderChange = (newProvider) => {
  console.log('Provider changed to:', newProvider)
  const selectedAgent = agentList.value.find(agent => agent.provider === newProvider)
  if (selectedAgent) {
    currentAgent.value = selectedAgent
    console.log('Current Agent updated to:', currentAgent.value)
  } else {
    currentAgent.value = null
    console.warn('No agent found for provider:', newProvider)
  }
}

const onModelChange = (newModelName) => {
  console.log('Model changed to:', newModelName)
  if (appConfig.value && appConfig.value.models) {
    const selectedModel = appConfig.value.models.find(model => model.name === newModelName)
    if (selectedModel) {
      currentModel.value = selectedModel
      console.log('Current Model updated to:', currentModel.value)
    } else {
      currentModel.value = null
      console.warn('No model found with name:', newModelName)
    }
  }
}

const filterModelsByProvider = computed(() => {
  if (!appConfig.value || !appConfig.value.models) return []
  return appConfig.value.models.filter(model => model.providers.includes(currentAgentProvider.value))
})

const shouldShowEditAgent = computed(() => {
  return currentAgent.value && currentAgent.value.editable
})

onMounted(loadAgentConfigs)
onMounted(loadAppConfig)

</script>

<style scoped>
.container {
  max-width: 800px;
  margin: auto;
  padding: 20px;
}
.section {
  margin-top: 20px;
}

.device-form {
  max-width: 1000px;
  margin: 0 auto;
  padding: 20px;
}
</style>
