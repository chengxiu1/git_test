import http from 'k6/http';
import { sleep, group, check } from 'k6';

const BASE_URL = 'http://159.75.122.40:8231';

// 生成单个随机中文字符
function getRandomChineseChar() {
    const unicodeRangeStart = 0x4E00; // 汉字的开始Unicode值
    const unicodeRangeEnd = 0x9FA5; // 汉字的结束Unicode值
    const randomUnicode = Math.floor(Math.random() * (unicodeRangeEnd - unicodeRangeStart + 1)) + unicodeRangeStart;
    return String.fromCharCode(randomUnicode);
}

// 生成指定长度的随机中文字符串
function getRandomChineseString(length) {
    let result = '';
    for (let i = 0; i < length; i++) { 
        result += getRandomChineseChar();
    }
    return result;
}

export const options = {
    thresholds: {
        'http_req_duration': ['p(95)<500'],
        'http_req_failed': ['rate<0.01'],
    },
    scenarios: { 
        contacts: { 
            executor: 'ramping-vus', 
            startVUs: 10, 
            stages: [ 
                { duration: '1m', target: 20 },  
                { duration: '3m', target: 0 }, 
            ],
            gracefulRampDown: '30s', 
        },
    },
};


// 登录函数
export function logon() {
    const url = BASE_URL + '/pams/front/login.do';
    const payload = 'loginName=student&password=student';
    const params = {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
    };
    let logon = http.post(url, payload, params);
    check(logon, {
        'login status is 200': (r) => r.status === 200,
    });
    sleep(Math.random() * 3 + 1);
}

// 保存供应商的函数
export function save_provider() {
    const url = '/pams/front/asset_provider/asset_provider_save.do';
    const webforms = 
        'id=&title=' + encodeURIComponent(getRandomChineseString(6)) + // 使用30个字符的随机中文字符串作为标题
        '&providerTypeId=2' + 
        '&providerName=' + encodeURIComponent(getRandomChineseString(5)) + // 使用5个字符的随机中文字符串作为供应商名称
        '&providerPhone=15345980111' + 
        '&providerAddress=' + encodeURIComponent('北京市某街道');
    
    const headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    };
    let res = http.post(BASE_URL + url, webforms, { headers: headers });

    check(res, {
        'save provider status is 200': (r) => r.status === 200,
        'save provider is ok': (r) => r.body.includes('OK'),
    });
    sleep(Math.random() * 3 + 1);
}

// 退出登录的函数
export function logout() {
    const url = BASE_URL + '/pams/front/logout.do';
    let logout = http.get(url);
    check(logout, {
        'logout status is 200': (r) => r.status === 200,
    });
    sleep(Math.random() * 3 + 1);
}

// 测试主函数
export default function () {
    logon();
    group('asset_provider', function() {
        sleep(10);
        save_provider();
    });
    logout();
}
