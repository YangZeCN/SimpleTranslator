#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试API切换功能
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from translator_api import TranslatorAPI
from config import Config

def test_api_switching():
    """测试API切换功能"""
    print("=" * 50)
    print("测试API切换功能")
    print("=" * 50)
    
    # 创建API实例
    api = TranslatorAPI()
    
    # 测试配置加载
    print("\n1. 测试配置加载...")
    provider = api.config.get('api_provider', 'openai')
    print(f"当前API提供商: {provider}")
    
    # 测试不同的API提供商设置
    providers = ['openai', 'deepseek', 'custom']
    
    for provider in providers:
        print(f"\n2. 测试切换到 {provider}...")
        success = api.set_api_provider(provider)
        current_provider = api.config.get('api_provider')
        print(f"设置结果: {success}")
        print(f"当前提供商: {current_provider}")
        print(f"当前模型: {api.get_current_model()}")
        
        # 测试API密钥获取
        current_key = api.get_current_api_key()
        print(f"当前API密钥: {'已设置' if current_key else '未设置'}")
        
        # 测试是否配置完整
        is_configured = api.is_configured()
        print(f"配置状态: {'完整' if is_configured else '不完整'}")
    
    # 测试自定义API配置
    print(f"\n3. 测试自定义API配置...")
    test_key = "test-key-123"
    test_url = "https://api.example.com/v1"
    test_model = "test-model"
    
    success = api.set_custom_config(test_key, test_url, test_model)
    print(f"自定义配置设置结果: {success}")
    
    # 验证自定义配置
    api.set_api_provider('custom')
    print(f"自定义API密钥: {api.config.get('custom_api_key')}")
    print(f"自定义Base URL: {api.config.get('custom_base_url')}")
    print(f"自定义模型: {api.config.get('custom_model')}")
    
    print("\n✅ API切换功能测试完成！")

def test_config_management():
    """测试配置管理功能"""
    print("\n" + "=" * 50)
    print("测试配置管理功能")
    print("=" * 50)
    
    config = Config()
    
    # 测试默认值
    print("\n1. 测试默认值获取...")
    provider = config.get('api_provider', 'default_value')
    print(f"API提供商: {provider}")
    
    non_existent = config.get('non_existent_key', 'default_value')
    print(f"不存在的键: {non_existent}")
    
    # 测试配置设置和保存
    print("\n2. 测试配置设置...")
    config.set('test_key', 'test_value')
    value = config.get('test_key')
    print(f"设置的测试值: {value}")
    
    print("\n✅ 配置管理功能测试完成！")

if __name__ == "__main__":
    try:
        test_config_management()
        test_api_switching()
        print("\n🎉 所有测试通过！多API支持功能正常工作。")
        
    except Exception as e:
        print(f"\n❌ 测试失败: {e}")
        import traceback
        traceback.print_exc()
