function sendInstructsApiRequest(instructionSet, sessionId, globalParams, ModName = 'free_other', ApiName = 'instruct') {
    // Send request to mod with instrumentsAPI
    // globalParams should be a dictionary of global instruction parameters
    // Add global instruction parameters to the instruction_parameters field of each instruction
    instructionSet.forEach(instruction => {
      instruction.instruction_parameters = { ...instruction.instruction_parameters, ...globalParams };
    });
  
    const params = {
      ModName: ModName,
      ApiName: ApiName,
      instruction_set: JSON.stringify(instructionSet),
      SessionID: sessionId
    };
  
    // Send request
    fetch('/api/mod', { method: 'POST', body: new URLSearchParams(params) })
      .then(response => {
        if (response.ok) {
          // Parse and return response data
          return response.json();
        } else {
          // Handle request error
          throw new Error('Request failed');
        }
      })
      .catch(error => {
        // Handle error
        console.error(error);
        return null;
      });
  }

// import axios from 'https://cdn.skypack.dev/axios';

// async function sendApiRequest(instructionSet, sessionId, globalParams, ModName = 'free_other', ApiName = 'instruct') {
//     // 将全局指令参数添加到每个指令的instruction_parameters字段中
//     instructionSet.forEach(instruction => {
//       instruction['instruction_parameters'] = { ...instruction['instruction_parameters'], ...globalParams };
//     });
  
//     const params = {
//       ModName: ModName,
//       ApiName: ApiName,
//       instruction_set: JSON.stringify(instructionSet),
//       SessionID: sessionId
//     };
  
//     try {
//       // 发送请求
//       const response = await axios.post('/api/mod', { params });
  
//       // 处理响应
//       if (response.status === 200) {
//         // 解析并返回响应数据
//         return response.data;
//       } else {
//         // 处理请求错误
//         return null;
//       }
//     } catch (error) {
//       // 处理请求错误
//       return null;
//     }
//   }