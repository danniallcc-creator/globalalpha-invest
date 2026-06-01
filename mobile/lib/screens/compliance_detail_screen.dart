import 'package:flutter/material.dart';

class ComplianceDetailScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('合规详情 & 转型建议')),
      body: ListView(
        padding: EdgeInsets.all(16),
        children: [
          _sectionHeader('当前品类：便携式储能系统'),
          _infoCard('准入红线 (Redline)', [
            '欧盟：必须符合 CE-EMC, LVD, RoHS 指令',
            '美国：UL 2743 (便携式电源) 强制认证',
            '海运：必须持有 UN38.3 报告及 MSDS',
          ], Colors.redAccent),
          _infoCard('转型建议 (Insight)', [
            '放弃低毛利单机，开发含太阳能充电板的“户外应急套餐”',
            '针对寒冷地区增加自加热电池技术',
            '配备移动 APP 远程管理功能，提高溢价',
          ], Colors.greenAccent),
        ],
      ),
    );
  }

  Widget _sectionHeader(String title) {
    return Padding(
      padding: EdgeInsets.symmetric(vertical: 16),
      child: Text(title, style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold)),
    );
  }

  Widget _infoCard(String title, List<String> items, Color color) {
    return Card(
      margin: EdgeInsets.only(bottom: 20),
      color: Colors.white.withOpacity(0.05),
      child: Padding(
        padding: EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(title, style: TextStyle(fontSize: 18, color: color, fontWeight: FontWeight.bold)),
            Divider(color: color.withOpacity(0.3)),
            ...items.map((e) => Padding(
              padding: EdgeInsets.symmetric(vertical: 4),
              child: Row(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text('• ', style: TextStyle(color: color, fontSize: 18)),
                  Expanded(child: Text(e, style: TextStyle(fontSize: 16, height: 1.4))),
                ],
              ),
            )).toList(),
          ],
        ),
      ),
    );
  }
}
