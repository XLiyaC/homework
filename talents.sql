/*
 Navicat MySQL Data Transfer

 Source Server         : test
 Source Server Type    : MySQL
 Source Server Version : 50717
 Source Host           : localhost:3306
 Source Schema         : talents

 Target Server Type    : MySQL
 Target Server Version : 50717
 File Encoding         : 65001

 Date: 20/12/2021 13:25:41
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for background
-- ----------------------------
DROP TABLE IF EXISTS `background`;
CREATE TABLE `background`  (
  `talentsID` char(8) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `education_grade` int(1) NOT NULL,
  `collegeID` char(8) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `majorID` char(8) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`talentsID`, `education_grade`) USING BTREE,
  INDEX `b_collegeid`(`collegeID`) USING BTREE,
  INDEX `b_majorid`(`majorID`) USING BTREE,
  INDEX `b_grade`(`education_grade`) USING BTREE,
  CONSTRAINT `b_grade` FOREIGN KEY (`education_grade`) REFERENCES `educationinfo` (`Grade`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `b_majorid` FOREIGN KEY (`majorID`) REFERENCES `major` (`ID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `b_talentsid` FOREIGN KEY (`talentsID`) REFERENCES `talentsinfo` (`ID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `b_collegeid` FOREIGN KEY (`collegeID`) REFERENCES `college` (`ID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of background
-- ----------------------------
INSERT INTO `background` VALUES ('P001', 1, 'U45', 'M15');
INSERT INTO `background` VALUES ('P001', 2, 'U16', 'M58');
INSERT INTO `background` VALUES ('P002', 1, 'U75', 'M42');
INSERT INTO `background` VALUES ('P002', 2, 'U87', 'M61');
INSERT INTO `background` VALUES ('P003', 1, 'U90', 'M01');
INSERT INTO `background` VALUES ('P003', 2, 'U65', 'M05');
INSERT INTO `background` VALUES ('P004', 1, 'U87', 'M54');
INSERT INTO `background` VALUES ('P004', 2, 'U87', 'M54');
INSERT INTO `background` VALUES ('P005', 1, 'U27', 'M57');
INSERT INTO `background` VALUES ('P005', 2, 'U87', 'M47');
INSERT INTO `background` VALUES ('P006', 1, 'U19', 'M65');
INSERT INTO `background` VALUES ('P007', 1, 'U20', 'M42');
INSERT INTO `background` VALUES ('P008', 1, 'U02', 'M42');
INSERT INTO `background` VALUES ('P009', 1, 'U41', 'M14');
INSERT INTO `background` VALUES ('P010', 1, 'U15', 'M06');
INSERT INTO `background` VALUES ('P010', 2, 'U72', 'M18');
INSERT INTO `background` VALUES ('P010', 3, 'U72', 'M32');
INSERT INTO `background` VALUES ('P011', 1, 'U41', 'M32');
INSERT INTO `background` VALUES ('P012', 1, 'U60', 'M29');
INSERT INTO `background` VALUES ('P012', 2, 'U28', 'M32');
INSERT INTO `background` VALUES ('P013', 1, 'U50', 'M50');
INSERT INTO `background` VALUES ('P013', 2, 'U35', 'M38');
INSERT INTO `background` VALUES ('P013', 3, 'U14', 'M42');
INSERT INTO `background` VALUES ('P014', 1, 'U89', 'M54');
INSERT INTO `background` VALUES ('P015', 1, 'U61', 'M62');
INSERT INTO `background` VALUES ('P015', 2, 'U01', 'M21');
INSERT INTO `background` VALUES ('P016', 1, 'U74', 'M51');
INSERT INTO `background` VALUES ('P017', 1, 'U40', 'M39');
INSERT INTO `background` VALUES ('P017', 2, 'U11', 'M39');
INSERT INTO `background` VALUES ('P018', 1, 'U04', 'M34');
INSERT INTO `background` VALUES ('P018', 3, 'U56', 'M60');
INSERT INTO `background` VALUES ('P019', 1, 'U17', 'M07');
INSERT INTO `background` VALUES ('P019', 2, 'U31', 'M23');
INSERT INTO `background` VALUES ('P020', 1, 'U21', 'M13');
INSERT INTO `background` VALUES ('P020', 2, 'U54', 'M13');
INSERT INTO `background` VALUES ('P021', 1, 'U81', 'M42');
INSERT INTO `background` VALUES ('P021', 2, 'U93', 'M42');
INSERT INTO `background` VALUES ('P021', 3, 'U93', 'M42');
INSERT INTO `background` VALUES ('P022', 1, 'U04', 'M20');
INSERT INTO `background` VALUES ('P022', 2, 'U68', 'M32');
INSERT INTO `background` VALUES ('P023', 1, 'U63', 'M35');
INSERT INTO `background` VALUES ('P023', 2, 'U10', 'M12');
INSERT INTO `background` VALUES ('P024', 1, 'U53', 'M42');
INSERT INTO `background` VALUES ('P025', 1, 'U46', 'M45');
INSERT INTO `background` VALUES ('P025', 2, 'U32', 'M46');
INSERT INTO `background` VALUES ('P026', 1, 'U64', 'M30');
INSERT INTO `background` VALUES ('P026', 2, 'U55', 'M06');
INSERT INTO `background` VALUES ('P027', 1, 'U83', 'M25');
INSERT INTO `background` VALUES ('P028', 1, 'U71', 'M04');
INSERT INTO `background` VALUES ('P029', 1, 'U05', 'M30');
INSERT INTO `background` VALUES ('P029', 2, 'U36', 'M32');
INSERT INTO `background` VALUES ('P030', 1, 'U41', 'M32');
INSERT INTO `background` VALUES ('P031', 1, 'U48', 'M31');
INSERT INTO `background` VALUES ('P031', 2, 'U38', 'M32');
INSERT INTO `background` VALUES ('P032', 1, 'U04', 'M42');
INSERT INTO `background` VALUES ('P032', 3, 'U22', 'M32');
INSERT INTO `background` VALUES ('P033', 1, 'U53', 'M42');
INSERT INTO `background` VALUES ('P034', 1, 'U03', 'M62');
INSERT INTO `background` VALUES ('P034', 2, 'U80', 'M23');
INSERT INTO `background` VALUES ('P035', 1, 'U81', 'M40');
INSERT INTO `background` VALUES ('P035', 2, 'U13', 'M32');
INSERT INTO `background` VALUES ('P035', 3, 'U13', 'M32');
INSERT INTO `background` VALUES ('P036', 1, 'U26', 'M42');
INSERT INTO `background` VALUES ('P036', 2, 'U26', 'M61');
INSERT INTO `background` VALUES ('P036', 3, 'U26', 'M03');
INSERT INTO `background` VALUES ('P037', 1, 'U87', 'M53');
INSERT INTO `background` VALUES ('P037', 2, 'U67', 'M24');
INSERT INTO `background` VALUES ('P038', 1, 'U53', 'M42');
INSERT INTO `background` VALUES ('P039', 1, 'U39', 'M16');
INSERT INTO `background` VALUES ('P039', 2, 'U07', 'M42');
INSERT INTO `background` VALUES ('P040', 1, 'U29', 'M43');
INSERT INTO `background` VALUES ('P040', 2, 'U08', 'M43');
INSERT INTO `background` VALUES ('P041', 1, 'U91', 'M42');
INSERT INTO `background` VALUES ('P041', 2, 'U85', 'M61');
INSERT INTO `background` VALUES ('P042', 1, 'U81', 'M02');
INSERT INTO `background` VALUES ('P042', 3, 'U73', 'M42');
INSERT INTO `background` VALUES ('P043', 1, 'U59', 'M62');
INSERT INTO `background` VALUES ('P043', 2, 'U67', 'M22');
INSERT INTO `background` VALUES ('P044', 1, 'U87', 'M64');
INSERT INTO `background` VALUES ('P044', 2, 'U87', 'M19');
INSERT INTO `background` VALUES ('P045', 1, 'U09', 'M42');
INSERT INTO `background` VALUES ('P046', 1, 'U47', 'M36');
INSERT INTO `background` VALUES ('P046', 2, 'U22', 'M42');
INSERT INTO `background` VALUES ('P047', 1, 'U11', 'M59');
INSERT INTO `background` VALUES ('P048', 1, 'U30', 'M41');
INSERT INTO `background` VALUES ('P048', 2, 'U49', 'M17');
INSERT INTO `background` VALUES ('P049', 1, 'U89', 'M06');
INSERT INTO `background` VALUES ('P049', 2, 'U89', 'M08');
INSERT INTO `background` VALUES ('P050', 1, 'U08', 'M42');
INSERT INTO `background` VALUES ('P051', 1, 'U88', 'M56');
INSERT INTO `background` VALUES ('P051', 2, 'U67', 'M22');
INSERT INTO `background` VALUES ('P052', 1, 'U42', 'M27');
INSERT INTO `background` VALUES ('P052', 2, 'U34', 'M06');
INSERT INTO `background` VALUES ('P053', 1, 'U18', 'M30');
INSERT INTO `background` VALUES ('P054', 1, 'U25', 'M52');
INSERT INTO `background` VALUES ('P055', 1, 'U15', 'M42');
INSERT INTO `background` VALUES ('P055', 3, 'U15', 'M33');
INSERT INTO `background` VALUES ('P056', 1, 'U04', 'M30');
INSERT INTO `background` VALUES ('P056', 3, 'U33', 'M42');
INSERT INTO `background` VALUES ('P057', 1, 'U41', 'M62');
INSERT INTO `background` VALUES ('P057', 2, 'U41', 'M06');
INSERT INTO `background` VALUES ('P058', 1, 'U58', 'M26');
INSERT INTO `background` VALUES ('P058', 2, 'U38', 'M66');
INSERT INTO `background` VALUES ('P059', 1, 'U06', 'M41');
INSERT INTO `background` VALUES ('P060', 1, 'U52', 'M62');
INSERT INTO `background` VALUES ('P060', 2, 'U52', 'M23');
INSERT INTO `background` VALUES ('P061', 2, 'U11', 'M39');
INSERT INTO `background` VALUES ('P062', 1, 'U49', 'M37');
INSERT INTO `background` VALUES ('P062', 2, 'U12', 'M42');
INSERT INTO `background` VALUES ('P062', 3, 'U12', 'M42');
INSERT INTO `background` VALUES ('P063', 1, 'U81', 'M41');
INSERT INTO `background` VALUES ('P063', 3, 'U33', 'M42');
INSERT INTO `background` VALUES ('P064', 1, 'U53', 'M42');
INSERT INTO `background` VALUES ('P064', 3, 'U69', 'M42');
INSERT INTO `background` VALUES ('P065', 1, 'U62', 'M30');
INSERT INTO `background` VALUES ('P065', 2, 'U16', 'M42');
INSERT INTO `background` VALUES ('P066', 1, 'U76', 'M42');
INSERT INTO `background` VALUES ('P066', 3, 'U66', 'M42');
INSERT INTO `background` VALUES ('P067', 1, 'U21', 'M42');
INSERT INTO `background` VALUES ('P067', 2, 'U44', 'M42');
INSERT INTO `background` VALUES ('P067', 3, 'U37', 'M42');
INSERT INTO `background` VALUES ('P068', 1, 'U50', 'M39');
INSERT INTO `background` VALUES ('P068', 2, 'U24', 'M44');
INSERT INTO `background` VALUES ('P068', 3, 'U24', 'M48');
INSERT INTO `background` VALUES ('P069', 1, 'U78', 'M30');
INSERT INTO `background` VALUES ('P069', 2, 'U51', 'M09');
INSERT INTO `background` VALUES ('P070', 1, 'U84', 'M28');
INSERT INTO `background` VALUES ('P070', 2, 'U82', 'M55');
INSERT INTO `background` VALUES ('P071', 1, 'U23', 'M62');
INSERT INTO `background` VALUES ('P071', 2, 'U79', 'M62');
INSERT INTO `background` VALUES ('P072', 1, 'U77', 'M42');
INSERT INTO `background` VALUES ('P073', 1, 'U11', 'M62');
INSERT INTO `background` VALUES ('P074', 1, 'U87', 'M63');
INSERT INTO `background` VALUES ('P074', 2, 'U67', 'M23');
INSERT INTO `background` VALUES ('P075', 1, 'U86', 'M10');
INSERT INTO `background` VALUES ('P075', 2, 'U43', 'M11');
INSERT INTO `background` VALUES ('P076', 1, 'U70', 'M40');
INSERT INTO `background` VALUES ('P077', 1, 'U57', 'M37');
INSERT INTO `background` VALUES ('P077', 2, 'U21', 'M40');
INSERT INTO `background` VALUES ('P078', 1, 'U92', 'M42');
INSERT INTO `background` VALUES ('P078', 2, 'U11', 'M49');
INSERT INTO `background` VALUES ('P079', 1, 'U75', 'M39');

-- ----------------------------
-- Table structure for college
-- ----------------------------
DROP TABLE IF EXISTS `college`;
CREATE TABLE `college`  (
  `ID` char(8) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `Name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `category` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `domestic` int(1) NULL DEFAULT NULL,
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of college
-- ----------------------------
INSERT INTO `college` VALUES ('U01', '阿拉巴马伯明翰分校', 'QS200以外', 0);
INSERT INTO `college` VALUES ('U02', '爱荷华州立大学', 'QS200以外', 0);
INSERT INTO `college` VALUES ('U03', '安徽医科大学', '双非', 1);
INSERT INTO `college` VALUES ('U04', '北京大学', '985', 1);
INSERT INTO `college` VALUES ('U05', '北京化工大学', '211', 1);
INSERT INTO `college` VALUES ('U06', '北京理工大学', '985', 1);
INSERT INTO `college` VALUES ('U07', '北卡罗莱纳州立大学', 'QS200以外', 0);
INSERT INTO `college` VALUES ('U08', '东北财经大学', '双非', 1);
INSERT INTO `college` VALUES ('U09', '东华大学', '211', 1);
INSERT INTO `college` VALUES ('U10', '东肯塔基大学', 'QS200以外', 0);
INSERT INTO `college` VALUES ('U11', '东南大学', '985', 1);
INSERT INTO `college` VALUES ('U12', '厄勒布鲁大学', 'QS200以外', 0);
INSERT INTO `college` VALUES ('U13', '佛罗里达大学', 'QS101-200', 0);
INSERT INTO `college` VALUES ('U14', '佛罗里达州立大学', 'QS200以外', 0);
INSERT INTO `college` VALUES ('U15', '复旦大学', '985', 1);
INSERT INTO `college` VALUES ('U16', '哥伦比亚大学', 'QS前100', 0);
INSERT INTO `college` VALUES ('U17', '哈尔滨医科大学', '双非', 1);
INSERT INTO `college` VALUES ('U18', '湖北大学', '双非', 1);
INSERT INTO `college` VALUES ('U19', '湖北中医药大学', '双非', 1);
INSERT INTO `college` VALUES ('U20', '湖南大学', '985', 1);
INSERT INTO `college` VALUES ('U21', '华东师范大学', '985', 1);
INSERT INTO `college` VALUES ('U22', '华盛顿大学', 'QS前100', 0);
INSERT INTO `college` VALUES ('U23', '华中科技大学同济医学院', '211', 1);
INSERT INTO `college` VALUES ('U24', '滑铁卢大学', 'QS101-200', 0);
INSERT INTO `college` VALUES ('U25', '淮海工学院', '双非', 1);
INSERT INTO `college` VALUES ('U26', '吉林大学', '985', 1);
INSERT INTO `college` VALUES ('U27', '吉林医科大学', '双非', 1);
INSERT INTO `college` VALUES ('U28', '加州大学伯克利分校', 'QS前100', 0);
INSERT INTO `college` VALUES ('U29', '江西财经大学', '双非', 1);
INSERT INTO `college` VALUES ('U30', '江西师范大学', '双非', 1);
INSERT INTO `college` VALUES ('U31', '利兹大学', 'QS前100', 0);
INSERT INTO `college` VALUES ('U32', '伦敦大学学院 / 圣何塞州立大学', 'QS前100', 0);
INSERT INTO `college` VALUES ('U33', '罗格斯大学', 'QS200以外', 0);
INSERT INTO `college` VALUES ('U34', '马来西亚博特拉大学', 'QS101-200', 0);
INSERT INTO `college` VALUES ('U35', '马萨诸塞大学洛威尔分校', 'QS200以外', 0);
INSERT INTO `college` VALUES ('U36', '迈阿密大学', 'QS200以外', 0);
INSERT INTO `college` VALUES ('U37', '密歇根州立大学', 'QS101-200', 0);
INSERT INTO `college` VALUES ('U38', '南京农业大学', '211', 1);
INSERT INTO `college` VALUES ('U39', '南京师范大学', '211', 1);
INSERT INTO `college` VALUES ('U40', '南京信息工程大学', '双非', 1);
INSERT INTO `college` VALUES ('U41', '南京医科大学', '双非', 1);
INSERT INTO `college` VALUES ('U42', '南京中医药学大学', '双非', 1);
INSERT INTO `college` VALUES ('U43', '南卡罗莱纳大学哥伦比亚分校', 'QS200以外', 0);
INSERT INTO `college` VALUES ('U44', '南开大学', '985', 1);
INSERT INTO `college` VALUES ('U45', '宁波诺丁汉大学', 'QS200以外', 0);
INSERT INTO `college` VALUES ('U46', '诺丁汉大学', 'QS前100', 0);
INSERT INTO `college` VALUES ('U47', '普渡大学', 'QS200以外', 0);
INSERT INTO `college` VALUES ('U48', '山西农业大学', '双非', 1);
INSERT INTO `college` VALUES ('U49', '上海财经大学', '211', 1);
INSERT INTO `college` VALUES ('U50', '上海大学', '211', 1);
INSERT INTO `college` VALUES ('U51', '上海海洋大学', '双非', 1);
INSERT INTO `college` VALUES ('U52', '上海交通大学', '985', 1);
INSERT INTO `college` VALUES ('U53', '上海师范大学', '双非', 1);
INSERT INTO `college` VALUES ('U54', '圣安德鲁斯大学', 'QS前100', 0);
INSERT INTO `college` VALUES ('U55', '圣路易斯华盛顿大学', 'QS101-200', 0);
INSERT INTO `college` VALUES ('U56', '石溪大学', 'QS200以外', 0);
INSERT INTO `college` VALUES ('U57', '苏州大学', '211', 1);
INSERT INTO `college` VALUES ('U58', '天津农学院', '双非', 1);
INSERT INTO `college` VALUES ('U59', '天津医科大学', '211', 1);
INSERT INTO `college` VALUES ('U60', '威斯康星大学欧克莱尔分校', 'QS200以外', 0);
INSERT INTO `college` VALUES ('U61', '温州医科大学', '双非', 1);
INSERT INTO `college` VALUES ('U62', '武汉大学', '985', 1);
INSERT INTO `college` VALUES ('U63', '西安交通大学', '985', 1);
INSERT INTO `college` VALUES ('U64', '西北农林科技大学', '985', 1);
INSERT INTO `college` VALUES ('U65', '香港城市大学', 'QS前100', 0);
INSERT INTO `college` VALUES ('U66', '香港大学', 'QS前100', 0);
INSERT INTO `college` VALUES ('U67', '香港中文大学', 'QS前100', 0);
INSERT INTO `college` VALUES ('U68', '辛辛那提大学医学院', 'QS200以外', 0);
INSERT INTO `college` VALUES ('U69', '亚利桑那大学', 'QS200以外', 0);
INSERT INTO `college` VALUES ('U70', '亚利桑那州立大学', 'QS200以外', 0);
INSERT INTO `college` VALUES ('U71', '盐城工学院', '双非', 1);
INSERT INTO `college` VALUES ('U72', '伊拉斯姆斯大学', 'QS101-200', 0);
INSERT INTO `college` VALUES ('U73', '伊利诺伊大学厄巴纳香槟分校', 'QS200以外', 0);
INSERT INTO `college` VALUES ('U74', '长春大学', '双非', 1);
INSERT INTO `college` VALUES ('U75', '浙江财经大学', '双非', 1);
INSERT INTO `college` VALUES ('U76', '浙江大学', '985', 1);
INSERT INTO `college` VALUES ('U77', '浙江工商大学', '双非', 1);
INSERT INTO `college` VALUES ('U78', '郑州轻工业大学', '双非', 1);
INSERT INTO `college` VALUES ('U79', '中国疾病预防控制中心', '研究院', 1);
INSERT INTO `college` VALUES ('U80', '中国疾控中心', '研究院', 1);
INSERT INTO `college` VALUES ('U81', '中国科学技术大学', '985', 1);
INSERT INTO `college` VALUES ('U82', '中国科学院巴斯德研究院', '研究院', 1);
INSERT INTO `college` VALUES ('U83', '中国矿业大学', '211', 1);
INSERT INTO `college` VALUES ('U84', '中国农业大学', '985', 1);
INSERT INTO `college` VALUES ('U85', '中国人民大学', '985', 1);
INSERT INTO `college` VALUES ('U86', '中国石油大学', '211', 1);
INSERT INTO `college` VALUES ('U87', '中国药科大学', '211', 1);
INSERT INTO `college` VALUES ('U88', '中国药科大学 ', '211', 1);
INSERT INTO `college` VALUES ('U89', '中国医科大学', '双非', 1);
INSERT INTO `college` VALUES ('U90', '中南大学', '985', 1);
INSERT INTO `college` VALUES ('U91', '中央财经大学', '211', 1);
INSERT INTO `college` VALUES ('U92', '仲恺农业工程学院', 'QS200以外', 0);
INSERT INTO `college` VALUES ('U93', '佐治亚大学', 'QS200以外', 0);

-- ----------------------------
-- Table structure for companyinfo
-- ----------------------------
DROP TABLE IF EXISTS `companyinfo`;
CREATE TABLE `companyinfo`  (
  `ID` char(8) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `Name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `Grade` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `Password` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `employee_num` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of companyinfo
-- ----------------------------
INSERT INTO `companyinfo` VALUES ('C01', 'Amgen', 'TOP Tier药厂', 'amgen1234', 3);
INSERT INTO `companyinfo` VALUES ('C02', 'Astellas', 'TOP Tier药厂', 'ast123887', 1);
INSERT INTO `companyinfo` VALUES ('C03', 'Covance', 'CRO', 'covance7', 4);
INSERT INTO `companyinfo` VALUES ('C04', 'Cstone Pharma', 'BioTech药厂', 'cstone56', 4);
INSERT INTO `companyinfo` VALUES ('C05', 'dMed', 'CRO', 'dmed9812', 12);
INSERT INTO `companyinfo` VALUES ('C06', 'Eli Lilly', 'TOP Tier药厂', 'eli761287', 5);
INSERT INTO `companyinfo` VALUES ('C07', 'Everest Clinical Research', 'CRO', 'everest2', 5);
INSERT INTO `companyinfo` VALUES ('C08', 'Fibro Gen', 'TOP Tier药厂', 'fibro9826', 1);
INSERT INTO `companyinfo` VALUES ('C09', 'Fosun', 'BioTech药厂', 'fosun7762', 4);
INSERT INTO `companyinfo` VALUES ('C10', 'Haihe Pharma', 'BioTech药厂', 'haihe2261', 4);
INSERT INTO `companyinfo` VALUES ('C11', 'Hutchinson', 'BioTech药厂', 'hut910273', 3);
INSERT INTO `companyinfo` VALUES ('C12', 'Junshi 君实', 'BioTech药厂', 'junshi543', 3);
INSERT INTO `companyinfo` VALUES ('C13', 'MSD', 'TOP Tier药厂', 'msd981232', 10);
INSERT INTO `companyinfo` VALUES ('C14', 'PPD', 'CRO', 'ppd012824', 5);
INSERT INTO `companyinfo` VALUES ('C15', 'PRA', 'CRO', 'pra982132', 6);
INSERT INTO `companyinfo` VALUES ('C16', 'R&G', 'CRO', 'rg9217620', 3);
INSERT INTO `companyinfo` VALUES ('C17', 'Roche', 'TOP Tier药厂', 'roche3921', 5);
INSERT INTO `companyinfo` VALUES ('C18', 'Zailab', 'BioTech药厂', 'zailab736', 1);

-- ----------------------------
-- Table structure for educationinfo
-- ----------------------------
DROP TABLE IF EXISTS `educationinfo`;
CREATE TABLE `educationinfo`  (
  `Grade` int(1) NOT NULL,
  `education` enum('本科','硕士','博士') CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`Grade`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of educationinfo
-- ----------------------------
INSERT INTO `educationinfo` VALUES (1, '本科');
INSERT INTO `educationinfo` VALUES (2, '硕士');
INSERT INTO `educationinfo` VALUES (3, '博士');

-- ----------------------------
-- Table structure for major
-- ----------------------------
DROP TABLE IF EXISTS `major`;
CREATE TABLE `major`  (
  `ID` char(8) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `Name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `statistic` int(1) NOT NULL DEFAULT 1,
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of major
-- ----------------------------
INSERT INTO `major` VALUES ('M01', '材料科学与工程', 0);
INSERT INTO `major` VALUES ('M02', '电子工程', 0);
INSERT INTO `major` VALUES ('M03', '概率论与数理统计', 1);
INSERT INTO `major` VALUES ('M04', '高分子材料', 0);
INSERT INTO `major` VALUES ('M05', '工商数据分析', 1);
INSERT INTO `major` VALUES ('M06', '公共卫生', 0);
INSERT INTO `major` VALUES ('M07', '公共卫生事业管理', 0);
INSERT INTO `major` VALUES ('M08', '公共卫生与预防医学', 1);
INSERT INTO `major` VALUES ('M09', '海洋生物学', 0);
INSERT INTO `major` VALUES ('M10', '环境工程', 0);
INSERT INTO `major` VALUES ('M11', '环境管理', 0);
INSERT INTO `major` VALUES ('M12', '基础医学', 0);
INSERT INTO `major` VALUES ('M13', '计算机', 1);
INSERT INTO `major` VALUES ('M14', '健康监察', 0);
INSERT INTO `major` VALUES ('M15', '金融财会管理', 0);
INSERT INTO `major` VALUES ('M16', '金融数学', 1);
INSERT INTO `major` VALUES ('M17', '金融统计', 1);
INSERT INTO `major` VALUES ('M18', '临床流行病学', 1);
INSERT INTO `major` VALUES ('M19', '临床药学', 0);
INSERT INTO `major` VALUES ('M20', '临床医学', 0);
INSERT INTO `major` VALUES ('M21', '流行病学', 1);
INSERT INTO `major` VALUES ('M22', '流行病学与生物统计', 1);
INSERT INTO `major` VALUES ('M23', '流行病学与卫生统计', 1);
INSERT INTO `major` VALUES ('M24', '流行病与卫生统计', 1);
INSERT INTO `major` VALUES ('M25', '煤矿工程', 0);
INSERT INTO `major` VALUES ('M26', '农学', 0);
INSERT INTO `major` VALUES ('M27', '涉外护理', 0);
INSERT INTO `major` VALUES ('M28', '生物', 0);
INSERT INTO `major` VALUES ('M29', '生物化学与分子生物学', 0);
INSERT INTO `major` VALUES ('M30', '生物技术', 0);
INSERT INTO `major` VALUES ('M31', '生物技术与经济', 0);
INSERT INTO `major` VALUES ('M32', '生物统计', 1);
INSERT INTO `major` VALUES ('M33', '生物统计与流行病学', 1);
INSERT INTO `major` VALUES ('M34', '生物物理与生理学', 0);
INSERT INTO `major` VALUES ('M35', '生物医学工程', 0);
INSERT INTO `major` VALUES ('M36', '食品科学', 0);
INSERT INTO `major` VALUES ('M37', '数理统计', 1);
INSERT INTO `major` VALUES ('M38', '数理统计与概率论', 1);
INSERT INTO `major` VALUES ('M39', '数学', 1);
INSERT INTO `major` VALUES ('M40', '数学与统计', 1);
INSERT INTO `major` VALUES ('M41', '数学与应用数学', 1);
INSERT INTO `major` VALUES ('M42', '统计', 1);
INSERT INTO `major` VALUES ('M43', '统计学', 1);
INSERT INTO `major` VALUES ('M44', '统计与数学', 1);
INSERT INTO `major` VALUES ('M45', '土木工程', 0);
INSERT INTO `major` VALUES ('M46', '土木工程 / 统计', 1);
INSERT INTO `major` VALUES ('M47', '微生物及生化制药', 0);
INSERT INTO `major` VALUES ('M48', '维度数学', 1);
INSERT INTO `major` VALUES ('M49', '系统工程', 0);
INSERT INTO `major` VALUES ('M50', '信息技术', 0);
INSERT INTO `major` VALUES ('M51', '信息与计算机', 1);
INSERT INTO `major` VALUES ('M52', '信息与系统管理', 0);
INSERT INTO `major` VALUES ('M53', '药剂学', 0);
INSERT INTO `major` VALUES ('M54', '药事管理', 0);
INSERT INTO `major` VALUES ('M55', '药物', 0);
INSERT INTO `major` VALUES ('M56', '药物分析', 0);
INSERT INTO `major` VALUES ('M57', '药学', 0);
INSERT INTO `major` VALUES ('M58', '应用分析', 1);
INSERT INTO `major` VALUES ('M59', '应用数学', 1);
INSERT INTO `major` VALUES ('M60', '应用数学与统计', 1);
INSERT INTO `major` VALUES ('M61', '应用统计', 1);
INSERT INTO `major` VALUES ('M62', '预防医学', 1);
INSERT INTO `major` VALUES ('M63', '制药工程', 0);
INSERT INTO `major` VALUES ('M64', '中药学', 0);
INSERT INTO `major` VALUES ('M65', '中药资源与开发', 0);
INSERT INTO `major` VALUES ('M66', '作物遗传育种', 0);

-- ----------------------------
-- Table structure for talentsinfo
-- ----------------------------
DROP TABLE IF EXISTS `talentsinfo`;
CREATE TABLE `talentsinfo`  (
  `ID` char(8) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `Name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `Top_grade` int(1) NULL DEFAULT NULL,
  `EntryTime` char(4) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `CompanyID` char(8) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `Password` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`ID`) USING BTREE,
  INDEX `t_companyid`(`CompanyID`) USING BTREE,
  INDEX `t_topgrade`(`Top_grade`) USING BTREE,
  CONSTRAINT `t_companyid` FOREIGN KEY (`CompanyID`) REFERENCES `companyinfo` (`ID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `t_topgrade` FOREIGN KEY (`Top_grade`) REFERENCES `educationinfo` (`Grade`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of talentsinfo
-- ----------------------------
INSERT INTO `talentsinfo` VALUES ('P001', '马天', 2, '2019', 'C13', 'mt6001');
INSERT INTO `talentsinfo` VALUES ('P002', '张希', 2, '2019', 'C09', 'zx6002');
INSERT INTO `talentsinfo` VALUES ('P003', '夏冬青', 2, '2016', 'C17', 'xdq6027');
INSERT INTO `talentsinfo` VALUES ('P004', '陈茵', 2, '2015', 'C09', 'cy6028');
INSERT INTO `talentsinfo` VALUES ('P005', '徐米拉', 2, '2018', 'C10', 'xml6082');
INSERT INTO `talentsinfo` VALUES ('P006', '沈是', 1, '2013', 'C15', 'ss6088');
INSERT INTO `talentsinfo` VALUES ('P007', '陈晨', 1, '2009', 'C15', 'cc7032');
INSERT INTO `talentsinfo` VALUES ('P008', '贾代', 1, '2015', 'C15', 'jd7033');
INSERT INTO `talentsinfo` VALUES ('P009', '张欣欣', 1, '2016', 'C11', 'zxx7091');
INSERT INTO `talentsinfo` VALUES ('P010', '魏迪', 3, '2015', 'C05', 'wd7099');
INSERT INTO `talentsinfo` VALUES ('P011', '汪洋', 1, '2008', 'C13', 'wy8003');
INSERT INTO `talentsinfo` VALUES ('P012', '林琳', 2, '1999', 'C07', 'll8004');
INSERT INTO `talentsinfo` VALUES ('P013', '张小北', 3, '2020', 'C17', 'zxb8009');
INSERT INTO `talentsinfo` VALUES ('P014', '赵诗文', 1, '2017', 'C09', 'zsw8034');
INSERT INTO `talentsinfo` VALUES ('P015', '赵小熙', 2, '2019', 'C17', 'zxx8069');
INSERT INTO `talentsinfo` VALUES ('P016', '卢帅', 1, '2008', 'C18', 'ls8091');
INSERT INTO `talentsinfo` VALUES ('P017', '黄迪文', 2, '2017', 'C05', 'hdw8092');
INSERT INTO `talentsinfo` VALUES ('P018', '林一一', 3, '2004', 'C06', 'lyy9001');
INSERT INTO `talentsinfo` VALUES ('P019', '张迪', 2, '2017', 'C07', 'zd9002');
INSERT INTO `talentsinfo` VALUES ('P020', '王也', 2, '2012', 'C13', 'wy9005');
INSERT INTO `talentsinfo` VALUES ('P021', '赵吏', 3, '2019', 'C06', 'zl9006');
INSERT INTO `talentsinfo` VALUES ('P022', '申屠元', 2, '2000', 'C14', 'sty9007');
INSERT INTO `talentsinfo` VALUES ('P023', '王则', 2, '2012', 'C01', 'wz9009');
INSERT INTO `talentsinfo` VALUES ('P024', '马九', 1, '2018', 'C03', 'mj9010');
INSERT INTO `talentsinfo` VALUES ('P025', '刘大伟', 2, '2017', 'C03', 'ldw9012');
INSERT INTO `talentsinfo` VALUES ('P026', '魏大', 2, '2020', 'C13', 'wd9016');
INSERT INTO `talentsinfo` VALUES ('P027', '万斯', 1, '2015', 'C09', 'ws9023');
INSERT INTO `talentsinfo` VALUES ('P028', '陈思', 1, '2013', 'C16', 'cs9024');
INSERT INTO `talentsinfo` VALUES ('P029', '吕文', 2, '2018', 'C15', 'lw9031');
INSERT INTO `talentsinfo` VALUES ('P030', '蔡赛迪', 1, '2016', 'C12', 'csd9032');
INSERT INTO `talentsinfo` VALUES ('P031', '张志文', 2, '2008', 'C13', 'zhang123456');
INSERT INTO `talentsinfo` VALUES ('P032', '王理清', 3, '2014', 'C13', 'wang121212');
INSERT INTO `talentsinfo` VALUES ('P033', '赵天', 1, '2016', 'C04', 'zhao343434');
INSERT INTO `talentsinfo` VALUES ('P034', '黎念青', 2, '2011', 'C06', 'lnq676789');
INSERT INTO `talentsinfo` VALUES ('P035', '黄蓉', 3, '2019', 'C06', 'hr121212');
INSERT INTO `talentsinfo` VALUES ('P036', '梅维锋', 3, '2019', 'C01', 'mwf125678');
INSERT INTO `talentsinfo` VALUES ('P037', '刘一君', 2, '2018', 'C15', 'lyj787878');
INSERT INTO `talentsinfo` VALUES ('P038', '周晓宇', 1, '2013', 'C05', 'zxy123456');
INSERT INTO `talentsinfo` VALUES ('P039', '刘炎林', 2, '2019', 'C07', 'lyl121212');
INSERT INTO `talentsinfo` VALUES ('P040', '王思云', 2, '2016', 'C05', 'wsy0912');
INSERT INTO `talentsinfo` VALUES ('P041', '宋紫云', 2, '2018', 'C05', 'szy0280');
INSERT INTO `talentsinfo` VALUES ('P042', '徐纯纯', 3, '2012', 'C04', 'xcc8021');
INSERT INTO `talentsinfo` VALUES ('P043', '刘文强', 2, '2019', 'C16', 'xwq9279');
INSERT INTO `talentsinfo` VALUES ('P044', '刘超', 2, '2018', 'C10', 'lc8172');
INSERT INTO `talentsinfo` VALUES ('P045', '章咪咪', 1, '2018', 'C05', 'zmm9120');
INSERT INTO `talentsinfo` VALUES ('P046', '潘佳栋', 2, '2017', 'C07', 'pjd7102');
INSERT INTO `talentsinfo` VALUES ('P047', '王石松', 1, '2009', 'C05', 'wss9102');
INSERT INTO `talentsinfo` VALUES ('P048', '朱丽娜', 2, '2013', 'C04', 'zln7621');
INSERT INTO `talentsinfo` VALUES ('P049', '刘萍', 2, '2020', 'C06', 'lp0112');
INSERT INTO `talentsinfo` VALUES ('P050', '汪洋', 1, '2015', 'C05', 'wy0123');
INSERT INTO `talentsinfo` VALUES ('P051', '周一桐', 2, '2018', 'C14', 'zyt8212');
INSERT INTO `talentsinfo` VALUES ('P052', '刘真', 2, '2017', 'C17', 'lz9211');
INSERT INTO `talentsinfo` VALUES ('P053', '宋婷婷', 1, '2013', 'C15', 'stt9270');
INSERT INTO `talentsinfo` VALUES ('P054', '朱松', 1, '2015', 'C14', 'zs6651');
INSERT INTO `talentsinfo` VALUES ('P055', '王红琳', 3, '2009', 'C05', 'whl0182');
INSERT INTO `talentsinfo` VALUES ('P056', '许虎', 3, '2014', 'C04', 'xh1972');
INSERT INTO `talentsinfo` VALUES ('P057', '刘蔷', 2, '2015', 'C13', 'lq1731');
INSERT INTO `talentsinfo` VALUES ('P058', '高华', 2, '2013', 'C12', 'gh9108');
INSERT INTO `talentsinfo` VALUES ('P059', '林致文', 1, '2016', 'C10', 'lzw7101');
INSERT INTO `talentsinfo` VALUES ('P060', '王名勋', 2, '2018', 'C02', 'wmx0021');
INSERT INTO `talentsinfo` VALUES ('P061', '李菱智', 2, '2015', 'C05', 'llz3083');
INSERT INTO `talentsinfo` VALUES ('P062', '戴榕', 3, '2017', 'C13', 'dr8210');
INSERT INTO `talentsinfo` VALUES ('P063', '许威华', 3, '2006', 'C03', 'xwh8211');
INSERT INTO `talentsinfo` VALUES ('P064', '张志鹏', 3, '2021', 'C13', 'zzp8716');
INSERT INTO `talentsinfo` VALUES ('P065', '徐奥利', 2, '2011', 'C12', 'xal9251');
INSERT INTO `talentsinfo` VALUES ('P066', '白帕琪', 3, '2016', 'C13', 'bpq8715');
INSERT INTO `talentsinfo` VALUES ('P067', '南方', 3, '2017', 'C01', 'nf8216');
INSERT INTO `talentsinfo` VALUES ('P068', '蒋无念', 3, '2015', 'C17', 'jwn8261');
INSERT INTO `talentsinfo` VALUES ('P069', '万艾', 2, '2015', 'C03', 'wa9721');
INSERT INTO `talentsinfo` VALUES ('P070', '吴拆其', 2, '2018', 'C08', 'wcq9716');
INSERT INTO `talentsinfo` VALUES ('P071', '图完', 2, '2017', 'C07', 'tw8750');
INSERT INTO `talentsinfo` VALUES ('P072', '朱爱玲', 1, '2016', 'C14', 'zal9292');
INSERT INTO `talentsinfo` VALUES ('P073', '陈易年', 1, '2016', 'C05', 'cyn0291');
INSERT INTO `talentsinfo` VALUES ('P074', '木凯瑞', 2, '2019', 'C16', 'mkr7162');
INSERT INTO `talentsinfo` VALUES ('P075', '热图', 2, '2014', 'C11', 'rt1972');
INSERT INTO `talentsinfo` VALUES ('P076', '鲁艾尔', 1, '2010', 'C10', 'lae9201');
INSERT INTO `talentsinfo` VALUES ('P077', '方一问', 2, '2008', 'C11', 'fyw0212');
INSERT INTO `talentsinfo` VALUES ('P078', '黄明军', 2, '2012', 'C05', 'hmj8120');
INSERT INTO `talentsinfo` VALUES ('P079', '卢巴尔', 1, '2017', 'C14', 'lbe1082');

-- ----------------------------
-- View structure for view_grade1
-- ----------------------------
DROP VIEW IF EXISTS `view_grade1`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `view_grade1` AS select `talentsinfo`.`EntryTime` AS `EntryTime`,count(`talentsinfo`.`Top_grade`) AS `本科` from `talentsinfo` where (`talentsinfo`.`Top_grade` = 1) group by `talentsinfo`.`EntryTime`;

-- ----------------------------
-- View structure for view_grade2
-- ----------------------------
DROP VIEW IF EXISTS `view_grade2`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `view_grade2` AS select `talentsinfo`.`EntryTime` AS `EntryTime`,count(`talentsinfo`.`Top_grade`) AS `硕士` from `talentsinfo` where (`talentsinfo`.`Top_grade` = 2) group by `talentsinfo`.`EntryTime`;

-- ----------------------------
-- View structure for view_grade3
-- ----------------------------
DROP VIEW IF EXISTS `view_grade3`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `view_grade3` AS select `talentsinfo`.`EntryTime` AS `EntryTime`,count(`talentsinfo`.`Top_grade`) AS `博士` from `talentsinfo` where (`talentsinfo`.`Top_grade` = 3) group by `talentsinfo`.`EntryTime`;

-- ----------------------------
-- View structure for view_gradetotal
-- ----------------------------
DROP VIEW IF EXISTS `view_gradetotal`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `view_gradetotal` AS select `talentsinfo`.`EntryTime` AS `EntryTime`,count(`talentsinfo`.`Top_grade`) AS `总人数` from `talentsinfo` group by `talentsinfo`.`EntryTime`;

-- ----------------------------
-- View structure for view_talents
-- ----------------------------
DROP VIEW IF EXISTS `view_talents`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `view_talents` AS select `talentsinfo`.`ID` AS `人才编号`,`talentsinfo`.`Name` AS `姓名`,`talentsinfo`.`CompanyID` AS `入职公司编号`,`companyinfo`.`Name` AS `公司名`,`talentsinfo`.`EntryTime` AS `入行年份`,`talentsinfo`.`Top_grade` AS `最高学历编号`,`educationinfo`.`education` AS `最高学历`,`college`.`Name` AS `学校名`,`college`.`category` AS `学校分类`,`college`.`domestic` AS `是否国内`,`major`.`Name` AS `专业名`,`major`.`statistic` AS `是否统计相关` from (((((`talentsinfo` left join `educationinfo` on((`educationinfo`.`Grade` = `talentsinfo`.`Top_grade`))) left join `companyinfo` on((`companyinfo`.`ID` = `talentsinfo`.`CompanyID`))) left join `background` on(((`background`.`talentsID` = `talentsinfo`.`ID`) and (`background`.`education_grade` = `educationinfo`.`Grade`)))) left join `college` on((`college`.`ID` = `background`.`collegeID`))) left join `major` on((`major`.`ID` = `background`.`majorID`)));

-- ----------------------------
-- Procedure structure for proc_comedu
-- ----------------------------
DROP PROCEDURE IF EXISTS `proc_comedu`;
delimiter ;;
CREATE PROCEDURE `proc_comedu`(comid CHAR(8))
SELECT education,COUNT(education) 人数 FROM talentsinfo JOIN educationinfo ON educationinfo.Grade = talentsinfo.Top_grade WHERE CompanyID=comid GROUP BY education
;;
delimiter ;

-- ----------------------------
-- Procedure structure for proc_cominfo
-- ----------------------------
DROP PROCEDURE IF EXISTS `proc_cominfo`;
delimiter ;;
CREATE PROCEDURE `proc_cominfo`(comid CHAR(8))
SELECT ID 公司编号,`Name` 公司名 ,Grade 公司分类,employee_num 入职员工数 FROM companyinfo
WHERE ID = comid
;;
delimiter ;

-- ----------------------------
-- Procedure structure for proc_selectedu
-- ----------------------------
DROP PROCEDURE IF EXISTS `proc_selectedu`;
delimiter ;;
CREATE PROCEDURE `proc_selectedu`(taid CHAR(8))
SELECT talentsID `人才编号`,talentsinfo.`Name` `姓名`,education `学历`,college.`Name` `学校名`,major.`Name` `专业名` FROM background JOIN talentsinfo ON talentsinfo.ID = background.talentsID JOIN educationinfo ON educationinfo.Grade = background.education_grade JOIN college ON college.ID = background.collegeID JOIN major ON major.ID = background.majorID 
WHERE talentsID = taid
ORDER BY talentsID
;;
delimiter ;

-- ----------------------------
-- Procedure structure for proc_selecttalents
-- ----------------------------
DROP PROCEDURE IF EXISTS `proc_selecttalents`;
delimiter ;;
CREATE PROCEDURE `proc_selecttalents`(taid CHAR(8))
SELECT `人才编号`, `姓名`, `入职公司编号`,`公司名`,`入行年份`,`最高学历`,`学校名`,`专业名` FROM view_talents WHERE `人才编号` = taid
;;
delimiter ;

-- ----------------------------
-- Procedure structure for proc_talents
-- ----------------------------
DROP PROCEDURE IF EXISTS `proc_talents`;
delimiter ;;
CREATE PROCEDURE `proc_talents`()
SELECT `人才编号`, `姓名`, `入职公司编号`,`公司名`,`入行年份`,`最高学历`,`学校名`,`专业名` FROM view_talents
;;
delimiter ;

-- ----------------------------
-- Procedure structure for proc_totaledu
-- ----------------------------
DROP PROCEDURE IF EXISTS `proc_totaledu`;
delimiter ;;
CREATE PROCEDURE `proc_totaledu`()
SELECT view_gradetotal.EntryTime,总人数, 本科,硕士,博士 FROM view_gradetotal LEFT JOIN view_grade1 ON view_gradetotal.EntryTime = view_grade1.EntryTime LEFT JOIN view_grade2 ON view_grade2.EntryTime=view_gradetotal.EntryTime LEFT JOIN view_grade3 ON view_grade3.EntryTime=view_gradetotal.EntryTime
;;
delimiter ;

SET FOREIGN_KEY_CHECKS = 1;
